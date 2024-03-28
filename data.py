import json
import numpy as np

matrixData = {}


def storeData(variableName, data):
    """Stores Data in the to the given matrixData dictionary

    Args:
        variableName (string): Key for matrixData
        data (matrix): Value for matrixData
    """
    matrixData[variableName] = data.tolist()
    with open('data.json', "w") as f:
        json.dump(matrixData, f)
    
def getData():
    """Gets Data from the matrixData dictionary

    Args:
        variableName (string): It's a given key for the matrixData dictionary 

    Returns:
        data: It helps in  getting the data of the specific key.
    """
    while True:
        try:
            with open('data.json', 'r') as f:
                mData = json.load(f)
            print(np.array(mData[input('Enter the variable name: ')]))
            break
        except FileNotFoundError:
            print(f"File '{mData.json}' not found. Please provide a valid filename.")
        except KeyError:
            print("Variable name not found. Please enter a valid variable name.")
        except json.JSONDecodeError:
            print("Error decoding JSON. File 'data.json' may be corrupted.")