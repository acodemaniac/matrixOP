from createMatrix import  zeroMatrix,userMatrix
from exitProgram import exitPro
from operations import veryGood

def menu():
    """This is MENU bar here is where you can select various options to perform your actions
    """
    while True:
        print("\n__MENU__")
        print("1. Create a Zero Matrix")
        print("2. Create a new user input Matrix")
        print("3. Matrix Operations")
        print("4. Exit the Program")

        choice = input("Enter your choice: ")
        actions = {
            '1': zeroMatrix,
            '2': userMatrix,
            '3': veryGood,
            '4': exitPro
        }
        action = actions.get(choice, lambda: print("Invalid choice"))
        action()


if __name__ == "__main__":
    menu()
