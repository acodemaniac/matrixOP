import numpy as np


def matrix():
    """Creates a Matrix with using Numpy Zeroes Function"""
    while True:
        try:
            rows, columns = map(int, input("Enter number of rows and columns (with space): ").split())
            A = np.zeros((rows, columns))
            print(A)
            if input("Is this the specified Matrix  --> Y/N ?").upper() == 'Y':
                break
        except ValueError:
            print("Please enter the new Rows & Columns")


matrix()
