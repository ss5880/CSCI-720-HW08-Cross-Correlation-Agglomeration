"""
@Author: Sumire Sakai, Tejal Shanbhag
@Purpose: To perform the Agglomeration of the data
"""

import numpy as np
import pandas as pd

global globalDataDict
Dendrogram_list={}


'''the  read_Data_file() reads datapoints from the csv file'''
def read_Data_file():
    data = pd.read_csv('HW_PCA_SHOPPING_CART_v896.csv')
    data = data.drop(['ID'], axis=1)
    columns = list(data.columns[1:])
    rows = list(data.iloc[:, 0])
    return data, rows, columns

'''getEuclideanDistance() calculates the Euclidean Distance between the points and returens the distance'''

def getEuclideanDistance(x, y):
    distance = np.sqrt(np.sum([(a - b) * (a - b) for a, b in zip(x, y)]))
    return distance

'''formatTheData() generates the global dictionary dataDict for acessing the points and after each iteration'''
def formatTheData(data, rows, coloumns):
    dataDict = {}
    #print(data.loc[0].values)
    for guest_index_x in range(0, len(rows)):
        dataDict[str(guest_index_x)] = data.loc[guest_index_x].values.tolist()
    return dataDict

'''generateDistanceMatrix() creates the Distance matrix for the points'''
def generateDistanceMatrix(data):
    dataKeys = data.keys()
    dataKeys = sorted(dataKeys)
    DISTANCE_MATRIX = {}
    for guest_index_x in range(0, len(dataKeys)):
        DISTANCE_MATRIX[str(guest_index_x)] = {}
        for guest_index_y in range(0, len(dataKeys)):
            if guest_index_x != guest_index_y:
                row1 = data[str(guest_index_x)]
                row2 = data[str(guest_index_y)]
                d = getEuclideanDistance(row1, row2)
                DISTANCE_MATRIX[str(guest_index_x)][str(guest_index_y)] = d
            else:
                DISTANCE_MATRIX[str(guest_index_x)][str(guest_index_y)] = float("inf")
    return DISTANCE_MATRIX
'''findClosestPoints finds the clusters with minimum distance'''
def findClosestPoints(DISTANCE_MATRIX):
    minDistance = float('inf')
    keys = DISTANCE_MATRIX.keys()
    guest1 = ''
    guest2 = ''
    keys = sorted(keys)
    for key_value_row in keys:
        row = DISTANCE_MATRIX[key_value_row]
        for key_value_col in row.keys():
            if (minDistance > row[key_value_col]):
                minDistance = row[key_value_col]
                guest1 = key_value_col
                guest2 = key_value_row
                #print(guest1,guest2,minDistance)
            #print(key_value_row, key_value_col, DISTANCE_MATRIX[key_value_row][key_value_col])
    return guest1,guest2



'''mergeGuests() combines the clusters with minimum distance and combines in the Distance Matrix'''
def mergeGuests(DISTANCE_MATRIX,guest1,guest2,dataDict):
    global Dendrogram_list
    Dendrogram_list[guest1]=guest2#Dictionary to record the clusters formed step by step
    # Delete the cluster1 and cluster2 from the DISTANCE_MATRIX and dataDict
    del (DISTANCE_MATRIX[guest1])
    del (DISTANCE_MATRIX[guest2])
    del(dataDict[guest1])
    del(dataDict[guest2])
    # Delete the distance of cluster1 and cluster2 from the DISTANCE_MATRIX and dataDict for each value in the dictionary
    for key in DISTANCE_MATRIX.keys():
        del (DISTANCE_MATRIX[key][guest1])
        del (DISTANCE_MATRIX[key][guest2])
    #find the average point value of the cluster
    avg_points=findAVG(guest1,guest2)
    mergedStr=str(guest1)+","+str(guest2)#string to add new record into DISTANCE_MATRIX
    dataDict[mergedStr]=avg_points#adding new point in dictionary
    DISTANCE_MATRIX[mergedStr]={}
    for keys in dataDict.keys():

        #calculating the distance of the new avg point and all the other points by iterating the keys of Dictionary
        if keys!=mergedStr:
            row1 = dataDict[keys]
            row2 = avg_points
            d = getEuclideanDistance(row1, row2)
            DISTANCE_MATRIX[mergedStr][keys] = d
            DISTANCE_MATRIX[keys][mergedStr] = d
        else:
            DISTANCE_MATRIX[mergedStr][keys] = float("inf")
    return DISTANCE_MATRIX,dataDict




'''findAVG() computes the average of the points in cluster guest1 and guest2 to form a new record
in the DISTANCE_MATRIX and the dataDict '''
def findAVG(guest1,guest2):
    global globalDataDict
    guests=guest1.split(",")+guest2.split(",")
    updatedAvgArray=[0]*len(globalDataDict[guests[0]])
    for i in guests:
        for j in range(len(globalDataDict[i])):
            updatedAvgArray[j] +=  (globalDataDict[i][j])/len(guests)
    return updatedAvgArray



'''startClustering() is the beginning of the Clustering process'''
def startClustering(DISTANCE_MATRIX,dataDict):
    finalClusters = []
    while len(dataDict.keys())>1:
        if(len(dataDict.keys())<=20):
            if(len(guest1.split(",")) < len(guest2.split(","))):
                finalClusters.append([int(guest) + 1 for guest in guest1[0].split(",")])
            else:
                finalClusters.append([int(guest) + 1 for guest in guest2[0].split(",")])
        guest1,guest2=findClosestPoints(DISTANCE_MATRIX)
        DISTANCE_MATRIX,dataDict=mergeGuests(DISTANCE_MATRIX,guest1,guest2,dataDict)
        if len(dataDict.keys())==6:
            print(dataDict)
    for cluster in range(len(finalClusters)):
        print("Cluster length" + str(20 - cluster) + ": " + str(len(finalClusters[cluster])))




def Main():
    global globalDataDict,Dendrogram_list
    data, rows, cols = read_Data_file()
    globalDataDict = formatTheData(data, rows, cols)
    dataDict_copy=globalDataDict.copy()
    GUEST_DISTANCE_MATRIX = generateDistanceMatrix(dataDict_copy)
    startClustering(GUEST_DISTANCE_MATRIX,dataDict_copy)
    #print(Dendrogram_list)

Main()
