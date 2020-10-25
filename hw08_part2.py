"""
@Author: Sumire Sakai, Tejal Shanbhag
@Purpose: To perform the Agglomeration of the data
"""

import pandas as pd

def read_crossCorr():
    data = pd.read_csv('Cross-Correlation Result.csv')
    columns=list(data.columns[1:])
    rows=list(data.iloc[:, 0])
    return data,rows,columns

def findMin(data,rows,col):
    for row_values in range(0,len(rows)):
        temp_row=list(data.iloc[row_values])
        min_row_value=min(temp_row[1:])
        min_row_idx=temp_row.index(min_row_value)
        print(min_row_value,min_row_idx,col[min_row_idx])





data,rows,cols=read_crossCorr()
findMin(data,rows,cols)