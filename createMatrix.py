import numpy as np
from data import matrixData

# ZERO MATRIX
def zeroMatrix():
    
    """Creates a Matrix with using Numpy Zeroes Function
    """
    global matrixData
    while True:
        try:
            mName = input("Enter the Matrix name/variable: ")
            rows, columns = map(int, input(
                "Enter number of rows and columns (with space): ").split())
            A = np.zeros((rows, columns))
            print(A)
            break
        except ValueError:
            print("Please enter valid rows and columns")
            
            

# USER DEFINED MATRIX
def userMatrix():
    print("User matrix")