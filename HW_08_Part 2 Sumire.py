import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import math
import Cluster as Cluster_Class

def readData():
    data = pd.read_csv('HW_PCA_SHOPPING_CART_v896.csv')
    data = data.iloc[:, [0, 3, 4]].values
    return data

def K_Means(data):
    clusters = convert_DF_to_Cluster(data)

    STOPPING_CRITERIA = 6
    N_CLUSTERS = data.shape[0]
    NUM_MERGED_CLUSTERS = 1

    while(N_CLUSTERS >= STOPPING_CRITERIA ):
        MIN_DISTANCE = math.inf
        MIN_DISTANCE_CLUSTER_1 = None
        MIN_DISTANCE_CLUSTER_2 = None

        for cluster1 in clusters:
            for cluster2 in clusters:
                distance = math.inf
                if isinstance(cluster1, Cluster_Class.Cluster) & isinstance(cluster2, Cluster_Class.Cluster):
                    if cluster1.User_ID != cluster2.User_ID:
                        distance = find_Euclidean_Distance(cluster1.x, cluster1.y, cluster2.x, cluster2.y)

                elif isinstance(cluster1, Cluster_Class.Cluster) & isinstance(cluster2, Cluster_Class.Marged_Cluster):
                    distance = find_Euclidean_Distance(cluster1.x, cluster1.y, cluster2.COM_x, cluster2.COM_y)

                elif isinstance(cluster1, Cluster_Class.Marged_Cluster) & isinstance(cluster2, Cluster_Class.Cluster):
                    distance = find_Euclidean_Distance(cluster1.COM_x, cluster1.COM_y, cluster2.x, cluster2.y)

                else: # cluster1: Merged_cluster && cluster2: Merged_cluster
                    if cluster1 != cluster2:
                        distance = find_Euclidean_Distance(cluster1.COM_x, cluster1.COM_y, cluster2.COM_x, cluster2.COM_y)

                if distance < MIN_DISTANCE:
                    MIN_DISTANCE = distance
                    MIN_DISTANCE_CLUSTER_1 = cluster1
                    MIN_DISTANCE_CLUSTER_2 = cluster2

        # if isinstance(MIN_DISTANCE_CLUSTER_1, Cluster_Class.Cluster):
        #     print("cluster")
        # else:
        #     print("merged")
        # if isinstance(MIN_DISTANCE_CLUSTER_2, Cluster_Class.Cluster):
        #     print("cluster")
        # else:
        #     print("merged")
        # print(MIN_DISTANCE_CLUSTER_1)
        # print(MIN_DISTANCE_CLUSTER_2)

        clusters.remove(MIN_DISTANCE_CLUSTER_1)
        clusters.remove(MIN_DISTANCE_CLUSTER_2)
        merged_cluster = merge_clusters(NUM_MERGED_CLUSTERS, MIN_DISTANCE_CLUSTER_1, MIN_DISTANCE_CLUSTER_2)

        if isinstance(MIN_DISTANCE_CLUSTER_1, Cluster_Class.Cluster) & isinstance(MIN_DISTANCE_CLUSTER_2, Cluster_Class.Cluster):
            COM = Cluster_Class.Marged_Cluster.get_com(MIN_DISTANCE_CLUSTER_1.x, MIN_DISTANCE_CLUSTER_1.y,
                                                       MIN_DISTANCE_CLUSTER_2.x, MIN_DISTANCE_CLUSTER_2.y)

        elif isinstance(MIN_DISTANCE_CLUSTER_1, Cluster_Class.Cluster) & isinstance(MIN_DISTANCE_CLUSTER_2, Cluster_Class.Marged_Cluster):
            COM = Cluster_Class.Marged_Cluster.get_com(MIN_DISTANCE_CLUSTER_1.x, MIN_DISTANCE_CLUSTER_1.y,
                                                       MIN_DISTANCE_CLUSTER_2.COM_x, MIN_DISTANCE_CLUSTER_2.COM_y)

        elif isinstance(MIN_DISTANCE_CLUSTER_1, Cluster_Class.Marged_Cluster) & isinstance(MIN_DISTANCE_CLUSTER_2, Cluster_Class.Cluster):
            COM = Cluster_Class.Marged_Cluster.get_com(MIN_DISTANCE_CLUSTER_1.COM_x, MIN_DISTANCE_CLUSTER_1.COM_y,
                                                       MIN_DISTANCE_CLUSTER_2.x, MIN_DISTANCE_CLUSTER_2.y)

        else:  # cluster1: Merged_cluster && cluster2: Merged_cluster
            COM = Cluster_Class.Marged_Cluster.get_com(MIN_DISTANCE_CLUSTER_1.COM_x, MIN_DISTANCE_CLUSTER_1.COM_y,
                                                       MIN_DISTANCE_CLUSTER_2.COM_x, MIN_DISTANCE_CLUSTER_2.COM_y)

        merged_cluster.COM_x = COM[0]
        merged_cluster.COM_y = COM[1]
        NUM_MERGED_CLUSTERS += 1
        clusters.append(merged_cluster)

        if N_CLUSTERS <= 20:
            print("Size is: ", MIN_DISTANCE_CLUSTER_1.size)
            print("Size is: ", MIN_DISTANCE_CLUSTER_2.size)
            for index in range(0, len(clusters)):
                print("Size of index ", index, " is ", clusters[index].size)

        print("Number of clusters: ", N_CLUSTERS)
        N_CLUSTERS -= 1




def merge_clusters(NUM_MERGED_CLUSTERS, MIN_DISTANCE_CLUSTER_1, MIN_DISTANCE_CLUSTER_2):
    merged_cluster = Cluster_Class.Marged_Cluster(NUM_MERGED_CLUSTERS, MIN_DISTANCE_CLUSTER_1, MIN_DISTANCE_CLUSTER_2)
    return merged_cluster

def convert_DF_to_Cluster(data):
    clusters = []
    for row in data:
        cluster = Cluster_Class.Cluster(row[0], row[1], row[2])
        clusters.append(cluster)

    return clusters

def find_Euclidean_Distance(cluster1_x, cluster1_y, cluster2_x, cluster2_y):
    distance = math.sqrt((cluster1_x - cluster1_y)**2 + ( cluster2_x - cluster2_y)**2)
    return distance

def main():
    data = readData()
    # clusters = convert_DF_to_Cluster(data)
    K_Means(data)

if __name__ == '__main__':
    main()
