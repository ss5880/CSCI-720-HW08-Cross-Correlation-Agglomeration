"""
@Author: Sumire Sakai, Tejal Shanbhag
@Purpose: To perform the Agglomeration of the data
"""

import pandas as pd
import numpy as np
def read_crossCorr():
    data = pd.read_csv('HW_PCA_SHOPPING_CART_v896.csv')
    columns=list(data.columns[1:])
    rows=list(data.iloc[:, 0])
    return data,rows,columns
def getEuclideanDistance(x,y):
    distance = np.sqrt(np.sum([(a - b) * (a - b) for a, b in zip(x, y)]))
    return distance

def generateDistanceMatrix(data,rows,coloumns):
    DISTANCE_MATRIX_GUEST=[[0 for guest_x in range(len(rows))]for guest_y in range(len(rows))]
    for guest_index_x in range(0, len(rows)):
        for guest_index_y in range(0, len(rows)):
            row1=data.loc[guest_index_x]
            row2=data.loc[guest_index_y]
            d=getEuclideanDistance(row1,row2)
            DISTANCE_MATRIX_GUEST[guest_index_x][guest_index_y]=d
            DISTANCE_MATRIX_GUEST[guest_index_y][guest_index_x] = d
    return DISTANCE_MATRIX_GUEST




data,rows,cols=read_crossCorr()
generateDistanceMatrix(data,rows,cols)