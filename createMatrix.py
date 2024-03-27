import numpy as np 
def zeroMatrix():
    
    """Creates a Matrix with using Numpy Zeroes Function
    """
    while True:
        try:
            rows, columns = map(int, input(
                "Enter number of rows and columns (with space): ").split())
            A = np.zeros((rows, columns))
            print(A)
            break
        except ValueError:
            print("Please enter valid rows and columns")
            
            
def userMatrix():
    print("User matrix")