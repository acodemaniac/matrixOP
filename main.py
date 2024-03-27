import numpy as np


def create_matrix():
    """Creates a Matrix with using Numpy Zeroes Function"""
    while True:

        rows, columns = map(int, input("Enter number of rows and columns (with space): ").split())
        A = np.zeros((rows, columns))
        
create_matrix()

