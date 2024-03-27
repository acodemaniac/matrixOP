matrixData = {}


def storeData(variableName, data):
    """Stores Data in the to the given matrixData dictionary

    Args:
        variableName (string): Key for matrixData
        data (matrix): Value for matrixData
    """
    matrixData[variableName] = data
    
def getData():
    """Gets Data from the matrixData dictionary

    Args:
        variableName (string): It's a given key for the matrixData dictionary 

    Returns:
        data: It helps in  getting the data of the specific key.
    """
    while True:
        try:
            variableName = input("Enter the variable name")
            return matrixData.get(variableName)
        except KeyError:
            print("Variable name not found. Please enter a valid variable name.")