
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        try:
            nb = int(argv[1])
            print("I am Even.") if nb % 2 == 0 else print("I am Odd.")
        except ValueError:
            print("AssertionError: argument is not an integer")
    elif len(argv) > 2:
        print("AssertionError: more than one argument is provided")
