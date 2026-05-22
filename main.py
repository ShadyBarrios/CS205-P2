from validate import validate
from enums import AlgoChoiceEnum

def main():
    print("Welcome to the (???) Feature Selection Algorithm")
    filename = input("Type the name of the file to test: ")
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            validFile = validate(lines) # testing with regex
            if not validFile:
                raise ValueError
            """
            need to get data and structure/normalize it
            """
    except (FileNotFoundError, FileExistsError, ValueError):
        print(f"Sorry, {filename} is not valid input. Try again.")
        return

    print("Type the name of the algorithm you want to run.")
    print("\t1) Forward Selection")
    print("\t2) Backward Selection")

    try:
        algoChoice = int(input("Choice: "))
        if algoChoice == 1:
            algoChoice = AlgoChoiceEnum.FORWARD
        elif algoChoice == 2:
            algoChoice = AlgoChoiceEnum.BACKWARD
        else:
            print("Invalid input. Try again.")
            return
        print(f"Algo Chosen: {algoChoice}")
    except ValueError:
        print("Invalid input type. Try again.")
        return

    """
    This dataset has x features (not including the class attribute), with y instances.
    """
if __name__ == "__main__":
    main()