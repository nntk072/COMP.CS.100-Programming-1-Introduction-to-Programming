"""Create a program that first reads 5 numbers a user enters and then prints, in the order the user entered them,
all the numbers that are greater than zero. An example of how the program operates: """


def main():
    """
    jfoiajfoijaoiwejfoijiewjfoawej
    """
    a = [0, 0, 0, 0, 0]
    print("Give 5 numbers:")
    for i in range(0, 5):
        a[i] = int(input("Next number: "))
    print("The numbers you entered that were greater than zero were:")
    for i in range(len(a)):
        if a[i] > 0:
            print(a[i])


if __name__ == "__main__":
    main()
