import numpy as np


def zeroMatrix():
    """Creates a Matrix with using Numpy Zeroes Function"""
    while True:
        try:
            rows, columns = map(int, input(
                "Enter number of rows and columns (with space): ").split())
            A = np.zeros((rows, columns))
            print(A)
            break
        except ValueError:
            print("Please enter valid rows and columns")


def performOP():
    print("performOP")


def userMatrix():
    print("User matrix")


def exitPro():
    """Function to exit the program"""
    print("Exiting...")
    quit()


def menu():
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
            '3': performOP,
            '4': exitPro
        }
        action = actions.get(choice, lambda: print("Invalid choice"))
        action()


if __name__ == "__main__":
    menu()
