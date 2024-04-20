import json
import time
import numpy as np

def addUser():
    """Creates a New User and Checks if the User Name already exists or not."""
    while True:
        try:
            username = input("Enter your new username: ")
            with open('data.json', 'r') as f:
                mData = json.load(f)
            if username in mData:
                print("Username already exists. Please choose a different one.")
            else:
                mData[username] = {
                    'zeroMatrix': {},
                    'identityMatrix': {},
                    'constantMatrix': {},
                    'scalarMatrix': {},
                    'userMatrix': {}
                }
                with open('data.json', 'w') as f:
                    json.dump(mData, f)
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
            username = input("Enter your username: ")
            with open('data.json', 'r') as f:
                mData = json.load(f)
            if username in mData:
                print("Loading profile...")
                time.sleep(1)
                print(f"Welcome back, {username}!")
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

def storeData(username, varName, tempData):
    """Stores Data in the given matrixData dictionary

    Args:
        username (string): User's username
        varName (string): Key for matrixData
        tempData (numpy.ndarray): Value for matrixData"""
    try:
        with open('data.json', 'r') as f:
            matrixData = json.load(f)
    except FileNotFoundError:
        print("Please enter a valid file name.")
        return

    matrixData[username][varName] = tempData.tolist()
    with open('data.json', 'w') as f:
        json.dump(matrixData, f)

def getData(username, matrixName):
    """Gets Data from the matrixData dictionary

    Args:
        username (string): User's username
        matrixName (string): Name of the matrix to retrieve

    Returns:
        numpy.ndarray: Data of the specified matrix"""
    while True:
        try:
            with open('data.json', 'r') as f:
                mData = json.load(f)
            variable_name = input('Enter the variable name: ')
            if variable_name not in mData[username][matrixName]:
                print("Variable name not found. Please enter a valid variable name.")
                continue
            return np.array(mData[username][matrixName][variable_name])
        except FileNotFoundError:
            print("File 'data.json' not found. Please provide a valid filename.")
        except json.JSONDecodeError:
            print("Error decoding JSON. File 'data.json' may be corrupted.")
        except KeyError:
            print("Key not found in JSON data.")
