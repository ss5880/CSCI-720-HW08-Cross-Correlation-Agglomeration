"""
@Author: Sumire Sakai, Tejal Shanbhag
@Purpose: To perform the Agglomeration of the data
"""

import pandas as pd

def read_crossCorr():
    data = pd.read_csv('HW_PCA_SHOPPING_CART_v896.csv')
    columns=list(data.columns[1:])
    rows=list(data.iloc[:, 0])
    return data,rows,columns

def generateDistanceMatrix(data,rows,coloumns):
    for i in range(0, len(rows)):
        row1=data.loc[i]
        row2=data.loc[i+1]
        print()




data,rows,cols=read_crossCorr()
generateDistanceMatrix(data,rows,cols)