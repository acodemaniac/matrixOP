import numpy as np
from data import matrixData,storeData

# ZERO MATRIX
def zeroMatrix():
    
    """Creates a Matrix with using Numpy Zeroes Function"""
    
    global matrixData
    while True:
        try:
            varName = input("Enter the Matrix name: ")
            rows, columns = map(int, input(f"Enter number of rows and columns (for {varName}: ").split())
            tempData = np.zeros((rows, columns))
            print(tempData)
            storeData(varName,tempData)
            
            break
        except ValueError:
            print("Please enter valid rows and columns")



# USER DEFINED MATRIX
def userMatrix():
    
    """Creates a user-defined matrix"""
    
    global matrixData
    while True:
        try:
            varName = input("Enter the Matrix name: ")
            rows, columns = map(int, input(
                "Enter number of rows and columns (with space): ").split())
            print(f"Enter elements for {varName}:")
            tempData = []
            for i in range(rows):
                row = []
                for j in range(columns):
                    element = float(input(f"Enter element at position ({i+1},{j+1}): "))
                    row.append(element)
                tempData.append(row)
            print("Matrix created successfully:")
            for row in tempData:
                print(row)
            storeData(varName, np.array(tempData))  
            break
        except ValueError:
            print("Please enter valid rows, columns, and elements")