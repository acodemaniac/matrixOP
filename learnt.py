import numpy as np


"""the given below code is very long so instead of this the best way was"""

rows,columns,dim=1,2,3 #user enters the input here
tempData = []
for i in range(rows):
    row = []
    for j in range(columns):
        column=[]
        for k in range(dim):
            element = float(input(f"Enter element at position ({i+1},{j+1},{k+1}): "))
            column.append(element)
        row.append(column)    
    tempData.append(row)

#best way to write the above code

tempData = np.array([[[float(input(f"Enter element at position ({i+1},{j+1},{k+1}): ")) for k in range(dim)] for j in range(columns)] for i in range(rows)])

print("Matrix created successfully:")