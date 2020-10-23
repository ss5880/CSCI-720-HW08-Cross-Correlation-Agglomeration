
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
    STRONGEST_CROSS_CORRELATION_VALUE = 0
    STRONGEST_CROSS_CORRELATION_ATTRIBUTE1 = None
    STRONGEST_CROSS_CORRELATION_ATTRIBUTE2 = None

    for columnName_x in columnNames:
        attribute_x = data[columnName_x]
        for columnName_y in columnNames:
            attribute_y = data[columnName_y]
            crossCorrelation_value  = attribute_x.corr(attribute_y)
            crossCorrelation_df.loc[columnName_y, columnName_x] = crossCorrelation_value

            if columnName_x != columnName_y:
                if crossCorrelation_value > STRONGEST_CROSS_CORRELATION_VALUE:
                    STRONGEST_CROSS_CORRELATION_VALUE = crossCorrelation_value
                    STRONGEST_CROSS_CORRELATION_ATTRIBUTE1 = columnName_x
                    STRONGEST_CROSS_CORRELATION_ATTRIBUTE2 = columnName_y

    print(STRONGEST_CROSS_CORRELATION_ATTRIBUTE1)
    print(STRONGEST_CROSS_CORRELATION_ATTRIBUTE2)
    # print(crossCorrelation_df.head())
    crossCorrelation_df.to_csv('Cross-Correlation Result.csv', index=True)
    return crossCorrelation_df

def analyzeAttribute(crossCorrelation_df, attributeName):
    # print((crossCorrelation_df.columns))
    colunNames = crossCorrelation_df.columns

    STRONGEST_CROSS_CORRELATION_VALUE = 0
    STRONGEST_CROSS_CORRELATION_ATTRIBUTE = None
    for attribute_y in colunNames:
        crossCorrelation_value = crossCorrelation_df.at[attribute_y, attributeName]
        if attribute_y != attributeName:
            if crossCorrelation_value > STRONGEST_CROSS_CORRELATION_VALUE:
                STRONGEST_CROSS_CORRELATION_VALUE = crossCorrelation_value
                STRONGEST_CROSS_CORRELATION_ATTRIBUTE = attribute_y

    print("Strongest Attribute with", attributeName, " is", STRONGEST_CROSS_CORRELATION_ATTRIBUTE)


def main():
    data = readData()
    crossCorrelation_df = compute_crossCorrelation( data )
    analyzeAttribute(crossCorrelation_df, '  Fish')
    analyzeAttribute(crossCorrelation_df, '  Meat')
    analyzeAttribute(crossCorrelation_df, ' Beans')

if __name__ == '__main__':
    main()