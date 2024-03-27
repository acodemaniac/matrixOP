matrixData = {}


def storeData(variableName, data):
    """Stores Data in the to the given matrixData dictionary

    Args:
        variableName (string): Key for matrixData
        data (matrix): Value for matrixData
    """
    matrixData[variableName] = data
    
def getData(variableName):
    """Gets Data from the matrixData dictionary

    Args:
        variableName (string): It's a given key for the matrixData dictionary 

    Returns:
        data: It helps in  getting the data of the specific key.
    """
    return matrixData.get(variableName)