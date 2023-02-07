"""Create a program that first prints the even numbers from 0 to 100 in an ascending order, and then the same numbers
in descending order. Each number is printed on its own row, so the program's printout looks like this: """


def main():
    for i in range(0, 101, 2):
        print(i)
    for i in range(100, -1, -2):
        print(i)


if __name__ == "__main__":
    main()
