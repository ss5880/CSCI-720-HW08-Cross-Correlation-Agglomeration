
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import math

def readData():
    data = pd.read_csv('HW_PCA_SHOPPING_CART_v896.csv')
    return data

def main():
    data = readData()

if __name__ == '__main__':
    main()