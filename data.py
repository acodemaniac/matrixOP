import json
import time

def addUser():
    """Creates a New User and Checks if the User Name already exists or not."""

    while True:
        try:
            userName = input("Enter your new username: ")
            with open('data.json', 'r') as f:
                mData = json.load(f)
            if userName in mData:
                print("Username already exists. Please choose a different one.")
            else:
                mData[userName] = {
                    'zeroMatrix': {},
                    'identityMatrix': {},
                    'constantMatrix': {},
                    'scalarMatrix': {},
                    'userMatrix': {}
                }
                with open('data.json', 'w') as f:
                    json.dump(mData, f)
                print("User added successfully!")
                break
        except FileNotFoundError:
            print("File not found. Please provide a valid file name.")
        except json.JSONDecodeError:
            print("Invalid JSON format in data file. Please ensure the file contains valid JSON.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

def existingUser():
    while True:
        try: 
            userName = input("Enter your username: ")
            with open('data.json', 'r') as f:
                mData = json.load(f)
            if userName in mData:
                print("Loading profile...")
                time.sleep(1)
                print(f"Welcome back, {userName}!")
                break
            else:
                print("Username does not exist. Please create an account.")
                addUser()
                break
        except FileNotFoundError:
            print("File not found. Please provide a valid file name.")
        except json.JSONDecodeError:
            print("Invalid JSON format in data file. Please ensure the file contains valid JSON.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

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