from createMatrix import newMatrix
from exitProgram import exitPro
from data import getData
# from operations import veryGood



def menu():
    """This is MENU bar here is where you can select various options to perform your actions
    """
    while True:
        print("\n__MENU__")
        print("1. Create a NewMatrix")
        # print("2. Create a ")
        print("3. Matrix Operations")
        print("4. Print the Matrix Data")
        print("5. Exit the Program")

        choice = input("Enter your choice: ")
        actions = {
            '1': newMatrix,
            # '2': something,
            # '3': veryGood,
            '4': getData,
            '5': exitPro
        }
        action = actions.get(choice, lambda: print("Invalid choice"))
        action()




if __name__ == "__main__":
    menu()