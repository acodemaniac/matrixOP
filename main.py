import sys
import time
from data import getData, addUser
from createMatrix import zeroMatrix, identityMatrix,scalarMatrix,constantMatrix,userMatrix

def exitPro():

    """Exits the Program Successfully"""

    if input("Are you sure you want to quit?  (y/n): ").lower() == 'y':
        print("\nThank You for using our program!\n")
        time.sleep(1)
        print("\t-Successful!!-")
        sys.exit(0)
    else:
        mainMenu()


def mainMenu():
    """This is MENU bar here is where you can select various options to perform your actions
    """
    
    try:
        question = input("Are you an existing user? (y/n)").upper()
        if user == 'Y':
            userName = input("Enter you name: ")
            existingUser(userName)
            None
        if user == 'N':
            userName = input("Enter your name: ")
            addUser(userName)
            print('\n...')
            time.sleep(1)
            print("Successfully added!" + userName)
            print(userName + ', welcome!')
    except ValueError:
        print("Please enter 'Y' for Yes or 'N' for No only.")

    while True:

        
        print("\n__MENU__")
        print("1. Create a NewMatrix")
        print("3. Matrix Operations")
        print("4. Load the Matrix Data")
        print("5. Exit the Program")

        choice = input("Enter your choice: ")
        actions = {
            '1': newMatrix,
            # '2': something,
            # '3': veryGood,
            '4': getOptions,
            '5': exitPro
        }
        action = actions.get(choice, lambda: print("Invalid choice"))
        action()

def newMatrix():

    """Creates a new matrix with user input for rows and columns"""

    while True:
        print("\n------------------------------")
        print("\n__New Matrix__")
        print("1. Create a zero matrix")
        print("2. Create an identity matrix")
        print("3. Create a constant matrix")
        print("4. Create a scalar matrix")
        print("5. Create a user input matrix")
        print("8. Go back to main menu")
        print("9. Exit the Program")

        choice = input("Enter your choice: ")
        actions = {
            '1': zeroMatrix,
            '2': identityMatrix,
            '3': constantMatrix, 
            '4': scalarMatrix,
            '5': userMatrix,
            '8': mainMenu,
            '9': exitPro
        }
        action = actions.get(choice, lambda : print("Invalid choice"))
        action()

def getOptions():
    """Options for get Data functions"""

    print("1. Get Your Data from 'Zero Matrix'")
    print("2. Get Your Data from 'Identity Matrix'")
    print("3. Get Your Data from 'Constant Matrix'")
    print("4. Get Your Data from 'Scalar Matrix'")
    print("5. Get Your Data from 'User Matrix'")

    matrices = {
        '1': 'zeroMatrix',
        '2': 'identityMatrix',
        '3': 'constantMatrix',
        '4': 'scalarMatrix',
        '5': 'userMatrix'
    }

    choice = input("Enter a choice to retrieve your data from: ")
    matrixName = matrices.get(choice, lambda : print("Invalid Choice"))
    getData(matrixName)


if __name__ == "__main__":
    mainMenu()