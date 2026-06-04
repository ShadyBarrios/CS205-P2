from validate import validate
from enums import AlgoChoiceEnum
from process import parse_data, normalize
from algorithms import run_algo, naive_algo

# txt/test_formatting_valid.txt

def main():
    # SAFA = Scott Andrew Football Associaton 
    print("Welcome to the SAFA Feature Selection Algorithm")
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
    dataset = parse_data(filename)
    if dataset is None:
        return
    dataset = normalize(dataset)
    num_instances = len(dataset)
    num_features = len(dataset[0].get_features())

    print(f"This dataset has {num_features} features (not including the class attribute), with {num_instances} instances.")

    """
    Running nearest neighbor with all x features, using "leave-one-out" evaluation,
    I get an accuracy of z.zz%.
    """
    naive_accuracy = naive_algo(dataset)
    print(f"Running nearest neighbor with all {num_features} features, using 'leave-one-out' evaluation,\nI get an accuracy of {(100*naive_accuracy):.2f}%.")
if __name__ == "__main__":
    main()