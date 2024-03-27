import numpy as np 

def matrix():
    """Creates a Matrix Function"""
    while True:
        try:
            rows=int(input("Number of rows :"))
            columns=int(input("Number of Columns: "))
            A = np.zeros((rows, columns))
            print(A)
            if input("Is this the specified Matrix  --> Y/N ?").upper() == 'Y':
                break
        except ValueError:
            print("Please enter the new Rows & Columns")
            
matrix()