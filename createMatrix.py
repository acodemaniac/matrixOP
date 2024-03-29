import numpy as np
from data import matrixData, storeData



def zeroMatrix():
    """Creates a Matrix using NumPy Zeroes Function"""

    try:
        varName = input("Enter the Matrix name: ")
        rows, columns, dim = map(int, input(f"Enter number of rows, columns and dimensions for {varName}: ").split())
        tempData = np.zeros((rows, columns, dim))
        print(tempData)
        storeData(varName, tempData)

    except ValueError:
        print("Please enter valid values for rows, columns and dimensions")

def identityMatrix():
    """Create an Identity Matrix"""

    try:
        varName = input("Enter the Matrix name: ")
        tempData = np.eye(int(input(f"Enter size of the identity matrix for {varName}: ")))
        print(tempData)
        storeData(varName, tempData)
    except ValueError:
        print("Please enter a valid size")

def constantMatrix():
    """Creates a Constant Matrix"""

    try:
        varName= input("Enter the Matrix Name: ")
        constant = int(input("Enter the constant: "))
        rows, columns, dim = map(int, input(f"Enter number of rows, columns and dimensions for {varName}: ").split())
        tempData = np.full_like(np.array(rows,columns),constant)
        print(tempData)
        storeData(varName, tempData)
    except ValueError:
        print("Please enter valid constant value, row and column. ")

def userMatrix():
    """Creates a user-defined matrix"""

    try:
        varName = input("Enter the Matrix name: ")
        rows, columns, dim = map(int, input(f"Enter number of rows, columns and dimensions for {varName} (with space): ").split())
        print(f"Enter elements for {varName}:")
        tempData = []
        tempData = np.array([[[float(input(f"Enter element at position ({i+1},{j+1},{k+1}): ")) for k in range(dim)] for j in range(columns)] for i in range(rows)])
        print("Matrix created successfully:")
        for row in tempData:
            print(row)
        storeData(varName, np.array(tempData))  
    except ValueError:
        print("Please enter valid rows, columns, and elements")

def scalarMatrix():
    """Calls the Identity Matrix and then multiplies the given number by it."""
    

    try:
        varName = input("Enter the Matrix name: ")
        size = int(input(f"Enter size of the identity matrix for {varName}: "))
        numb =int(input("Enter the multiplication number: "))
        tempData = np.eye(size)
        tempData*=numb
        print(tempData)
        storeData(varName, tempData)
    except ValueError:
        print("Please enter a valid size")