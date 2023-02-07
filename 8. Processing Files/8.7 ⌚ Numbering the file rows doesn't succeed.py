"""
Create a program that reads a file and prints its contents with each row starts with the row's number and a space.
"""


def main():
    a = input("Enter the name of the file: ")
    try:
        file = open(a, mode="r")
    except:
        print("There was an error in reading the file.")


if __name__ == "__main__":
    main()
