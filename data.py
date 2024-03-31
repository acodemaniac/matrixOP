import json
import numpy as np

def addUser(userName):
    try:
        with open('data.json', 'r') as f:
            matrixData = json.load(f)
        matrixData[userName] = {
            'zeroMatrix' : {},
            'identityMatrix' : {},
            'constantMatrix': {},
            'scalarMatrix' : {},
            'userMatrix' : {}
            }
    except FileNotFoundError:
            print("Please enter  a valid file name.")
        

def storeData(funName, varName, tempData):
    """Stores Data in the given matrixData dictionary

    Args:
        variableName (string): Key for matrixData
        data (matrix): Value for matrixData"""

    try:
        with open('data.json', 'r') as f:
            matrixData = json.load(f)
    except FileNotFoundError:
            print("Please enter  a valid file name.")
    matrixData[funName][varName] = tempData.tolist()
    with open('data.json', 'w') as f:
        json.dump(matrixData, f)

def getData(matrixName):
    """Gets Data from the matrixData dictionary

    Args:
        variableName (string): It's a given key for the matrixData dictionary 

    Returns:
        data: It helps in  getting the data of the specific key."""

    while True:
        
        try:
            with open('data.json', 'r') as f:
                mData = json.load(f)
            print(np.array(mData[matrixName][input('Enter the variable name: ')]))
            break
        except FileNotFoundError:
            print(f"File '{mData.json}' not found. Please provide a valid filename.")
        except KeyError:
            print("Variable name not found. Please enter a valid variable name.")
        except json.JSONDecodeError:
            print("Error decoding JSON. File 'data.json' may be corrupted.")