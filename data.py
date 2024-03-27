matrixData = {}


def storeData(variable_name, data):
    matrixData[variable_name] = data
    
def getData(variable_name):
    return matrixData.get(variable_name, None)
    