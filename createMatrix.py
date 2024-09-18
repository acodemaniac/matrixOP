import numpy as np
from data import storeData





def zeroMatrix():
    """Creates a Matrix using NumPy Zeroes Function"""
    while True:
        try:
            varName = input("Enter the Matrix name: ")
            rows = int(input(f"Enter number of rows for {varName}: "))
            columns = int(input(f"Enter number of columns for {varName}: "))
            dim = int(input(f"Enter number of dimensions for {varName}: "))
            if input("Do you want to store this data? (y/n): ").lower() == 'y':
                tempData = np.zeros((rows, columns, dim))
            print(tempData)
            storeData("zeroMatrix", varName, tempData)
            break
        except ValueError:
            print("Please enter valid integer values for rows, columns, and dimensions")
        except TypeError:
            print("Please enter a valid integer!")


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
        except TypeError:
            print("Please enter a valid integer!")

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
        except TypeError:
            print("Please enter a valid integer!")            

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
        except TypeError:
            print("Please enter a valid integer!")

def scalarMatrix():
    """Calls the Identity Matrix and then multiplies the given number by it."""
    

    while True:
        try:
            varName = input("Enter the Matrix name: ")
            size = int(input(f"Enter size of the identity matrix for {varName}: "))
            numb =int(input("Enter the multiplication number: "))
            tempData = np.eye(size)
            tempData*=numb
            print(tempData)
            storeData(varName, tempData)
            break
        except ValueError:
            print("Please enter a valid size")
        except TypeError:
            print("Please enter a valid integer!")


