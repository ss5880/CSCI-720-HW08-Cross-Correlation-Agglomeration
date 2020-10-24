
"""
@Author: Sumire Sakai, Tejal Shanbhag
@Purpose: To calculate the cross-correlation
"""
import pandas as pd
import numpy as np
import math

"""
Read the CSV file, convert it into dataFrame and drop the unique attribute
Return dataFrame 
"""
def readData():
    data = pd.read_csv('HW_PCA_SHOPPING_CART_v896.csv')
    data = data.drop(['ID'], axis=1)

    return data

"""
Calculate the Correlation for each other attribute and store it in new DataFrame
data: (dataFrame) data from CSV file
return Created new DataFrame with calculated correlation in the cells 
"""
def compute_crossCorrelation(data):
    # take the all attributes name
    columnNames = data.columns

    # Create a new DataFrame by using attribute names for columns and rows
    crossCorrelation_df = pd.DataFrame(columns=columnNames, index= columnNames)

    # Initialize the variable
    STRONGEST_CROSS_CORRELATION_VALUE = 0
    STRONGEST_CROSS_CORRELATION_ATTRIBUTE1 = None
    STRONGEST_CROSS_CORRELATION_ATTRIBUTE2 = None

    # Loop over columns
    for columnName_x in columnNames:
        attribute_x = data[columnName_x]

        # Loop over rows
        for columnName_y in columnNames:
            attribute_y = data[columnName_y]

            # Calculate the attribute
            crossCorrelation_value  = attribute_x.corr(attribute_y)

            # Store in the new DataFrame
            crossCorrelation_df.loc[columnName_y, columnName_x] = crossCorrelation_value

            # If column name and row name are not same
            if columnName_x != columnName_y:

                # Compare the correlation to find the highest correlation point
                if abs(crossCorrelation_value) > STRONGEST_CROSS_CORRELATION_VALUE:
                    STRONGEST_CROSS_CORRELATION_VALUE = abs(crossCorrelation_value)
                    STRONGEST_CROSS_CORRELATION_ATTRIBUTE1 = columnName_x
                    STRONGEST_CROSS_CORRELATION_ATTRIBUTE2 = columnName_y

    print("Strongest Correlation Attribute 1: ", STRONGEST_CROSS_CORRELATION_ATTRIBUTE1)
    print("Strongest Correlation Attribute 2: ", STRONGEST_CROSS_CORRELATION_ATTRIBUTE2)
    print("")

    # Initialize the variable
    LEAST_CROSS_CORRELATION_VALUE = math.inf
    LEAST_CROSS_CORRELATION_ATTRIBUTE = None

    # Create a new DataFrame with column names from csv data
    correlation_sum_df = pd.DataFrame(columns=columnNames)
    for columnName in columnNames:
        attribute_correlation_sum = 0

        # Loop over rows to take the sum of absolute correlation value
        for row in crossCorrelation_df[columnName]:
            attribute_correlation_sum += abs(row)

        # Store the total same of absolute correlation value in the new DataFrame
        correlation_sum_df.loc[1, columnName] = attribute_correlation_sum - 1

    # Compare the total sum of absolute correlation to get the value closest to 0
    for columnName in correlation_sum_df.columns:
        correlation = correlation_sum_df.loc[1, columnName]
        if correlation < LEAST_CROSS_CORRELATION_VALUE:
            LEAST_CROSS_CORRELATION_VALUE = correlation
            LEAST_CROSS_CORRELATION_ATTRIBUTE = columnName

    print("Least Correlation Attribute:\t\t", LEAST_CROSS_CORRELATION_ATTRIBUTE)
    print("Sum of Correlation is: ", LEAST_CROSS_CORRELATION_VALUE)

    # Drop the Least correlated attribute from the DataFrame to get the second least correlated attribute
    corralation_sum_df = correlation_sum_df.drop([LEAST_CROSS_CORRELATION_ATTRIBUTE], axis=1)

    # Initialize the variable
    SECOND_LEAST_CROSS_CORRELATION_VALUE = math.inf
    SECOND_LEAST_CROSS_CORRELATION_ATTRIBUTE = None

    # Compare the total sum of absolute correlation to get the value closest to 0
    for columnName in corralation_sum_df.columns:
        correlation = corralation_sum_df.loc[1, columnName]
        if correlation < SECOND_LEAST_CROSS_CORRELATION_VALUE:
            SECOND_LEAST_CROSS_CORRELATION_VALUE = correlation
            SECOND_LEAST_CROSS_CORRELATION_ATTRIBUTE = columnName

    print("Second Least Correlation Attribute: ", SECOND_LEAST_CROSS_CORRELATION_ATTRIBUTE)
    print("Sum of Correlation is: ", SECOND_LEAST_CROSS_CORRELATION_VALUE)
    print("")

    # crossCorrelation_df.to_csv('Cross-Correlation Result.csv', index=True)
    return crossCorrelation_df

"""
This function returns the attribute which is most strongly correlated attribute
crossCorrelation: (DataFrame) contains all caluclated cross-correlation values
attributeNate: (string) attribute name that we want to find the most strongly correlated attribute
"""
def analyzeAttribute(crossCorrelation_df, attributeName):

    # Get the column names from DataFrame
    colunNames = crossCorrelation_df.columns

    # Initialize the variable
    STRONGEST_CROSS_CORRELATION_VALUE = 0
    STRONGEST_CROSS_CORRELATION_ATTRIBUTE = None

    # Loop over column
    for attribute_y in colunNames:

        # Get the correlation value
        crossCorrelation_value = crossCorrelation_df.at[attribute_y, attributeName]

        # Ignore if column name is same with row name
        if attribute_y != attributeName:

            # take the absolute correlation and compare values to get the highest cross-correlation value
            if abs(crossCorrelation_value) > STRONGEST_CROSS_CORRELATION_VALUE:
                STRONGEST_CROSS_CORRELATION_VALUE = abs(crossCorrelation_value)
                STRONGEST_CROSS_CORRELATION_ATTRIBUTE = attribute_y

    print("Strongest Attribute with", attributeName, " is", STRONGEST_CROSS_CORRELATION_ATTRIBUTE)

"""
Main function which calls every functions
"""
def main():

    # Read data
    data = readData()

    # calculate the cross-correlated value and store it in DataFrame and return the DataFrame
    crossCorrelation_df = compute_crossCorrelation( data )

    # To know which attribute has the strong correlation with the specified attribute
    analyzeAttribute(crossCorrelation_df, '  Fish')
    analyzeAttribute(crossCorrelation_df, '  Meat')
    analyzeAttribute(crossCorrelation_df, ' Beans')

if __name__ == '__main__':
    main()