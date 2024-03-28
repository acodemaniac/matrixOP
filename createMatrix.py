import numpy as np
from data import matrixData, storeData
from main import menu
def newMatrix():

    """Creates a new matrix with user input for rows and columns"""

    while True:
        print("\n------------------------------")
        print("\n__New Matrix__")
        print("1. Create a zero matrix")
        print("2. Create an identity matrix")
        print("3. Create a constant matrix")
        print("4. Create a scalar matrix")
        print("5. Create a user input matrix")
        

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
                    tempData = np.eye(int(input(f"Enter size of the identity matrix for {varName}: ")))
                    print(tempData)
                    storeData(varName, tempData)
                    break
                except ValueError:
                    print("Please enter a valid size")

        def constantMatrix():
            """Creates a Constant Matrix"""
            while True:
                try:
                    varName= input("Enter the Matrix Name: ")
                    constant = int(input("Enter the constant: "))
                    rows, columns, dim = map(int, input(f"Enter number of rows, columns and dimensions for {varName}: ").split())
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
                    rows, columns, dim = map(int, input(f"Enter number of rows, columns and dimensions for {varName} (with space): ").split())
                    print(f"Enter elements for {varName}:")
                    tempData = []
                    tempData = np.array([[[float(input(f"Enter element at position ({i+1},{j+1},{k+1}): ")) for k in range(dim)] for j in range(columns)] for i in range(rows)])
                    print("Matrix created successfully:")
                    for row in tempData:
                        print(row)
                    storeData(varName, np.array(tempData))  
                    break
                except ValueError:
                    print("Please enter valid rows, columns, and elements")

        def scalarMatrix():
            """Calls the Identity Matrix and then multiplies the given number by it."""
            tempData = identityMatrix()
            num = float(input("Enter a Number"))
            scaMat = tempData*num
            

        choice = input("Enter your choice: ")
        actions = {
            '1': zeroMatrix,
            '2': identityMatrix,
            '3': constantMatrix, 
            '4': scalarMatrix,
            '5': userMatrix
        }
        action = actions.get(choice, lambda: print("Invalid choice"))
        action()