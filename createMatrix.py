import numpy as np
from data import matrixData, storeData  
def newMatrix():

    """Creates a new matrix with user input for rows and columns"""

    while True:
        print("\n------------------------------")
        print("\n__New Matrix__")
        print("1. Create a zero matrix")
        print("2. Create an identity matrix")
        print("3. Create a scalar matrix")
        print("4. Create a user input matrix")

        def zeroMatrix():
            """Creates a Matrix with using Numpy Zeroes Function"""
            while True:
                try:
                    varName = input("Enter the Matrix name: ")
                    rows, columns, dim = map(int, input(f"Enter number of rows, columns and dimensions for {varName}: ").split())
                    tempData = np.zeros((rows, columns, dim))
                    print(tempData)
                    storeData(varName, tempData)
                    break
                except ValueError:
                    print("Please enter valid rows and columns")

        def identityMatrix():
            """Create an Identity Matrix"""
            while True:
                try:
                    varName = input("Enter the Matrix name: ")
                    size = int(input(f"Enter size of the identity matrix for {varName}: "))
                    tempData = np.eye(size)
                    print(tempData)
                    storeData(varName, tempData)
                    break
                except ValueError:
                    print("Please enter a valid size")

        def constantMatrix():
            """Creates a Scalar Matrix"""
            while True:
                try:
                    varName= input("Enter the Matrix Name: ")
                    constant = int(input("Enter the constant: "))
                    rows, columns = map(int, input(f"Enter number of rows and columns for {varName}: ").split())
                    tempData = np.full_like(np.array(rows,columns),constant)
                    print(tempData)
                    storeData(varName, tempData)
                    break
                except ValueError:
                    print("Please enter valid constant value, row and column. ")

        def userMatrix():
            """Creates a user-defined matrix"""
            while True:
                try:
                    varName = input("Enter the Matrix name: ")
                    rows, columns = map(int, input(
                        f"Enter number of rows and columns for {varName} (with space): ").split())
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

        choice = input("Enter your choice: ")
        actions = {
            '1': zeroMatrix,
            '2': identityMatrix,
            '3': constantMatrix, 
            '4': userMatrix
        }
        action = actions.get(choice, lambda: print("Invalid choice"))
        action()