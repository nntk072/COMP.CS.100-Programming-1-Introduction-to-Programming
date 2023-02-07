"""
Create a program that reads a file and prints its contents with each row starts with the row's number and a space.
"""


def main():
    a = input("Enter the name of the file: ")
    file = open(a, mode="r")
    k = 0
    for i in file:
        if i.strip() or i.split() == []:
            k += 1
        i = i.rstrip()
        print(f"{k} {i}")
    file.close()


if __name__ == "__main__":
    main()
