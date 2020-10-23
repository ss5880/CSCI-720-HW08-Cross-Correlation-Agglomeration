
import pandas as pd
import numpy as np

def readData():
    data = pd.read_csv('HW_PCA_SHOPPING_CART_v896.csv')
    data = data.drop(['ID'], axis=1)
    # print(data.head())

    return data

def compute_crossCorrelation(data):
    columnNames = data.columns
    crossCorrelation_df = pd.DataFrame(columns=columnNames, index= columnNames)
    # print(crossCorrelation_df.head())

    for columnName_x in columnNames:
        attribute_x = data[columnName_x]
        for columnName_y in columnNames:
            attribute_y = data[columnName_y]
            crossCorrelation_value  = attribute_x.corr(attribute_y)
            crossCorrelation_df.loc[columnName_x, columnName_y] = crossCorrelation_value
    print(crossCorrelation_df.head())
    crossCorrelation_df.to_csv('Cross-Correlation Result.csv', index=True)

def main():
    data = readData()
    compute_crossCorrelation( data )

if __name__ == '__main__':
    main()