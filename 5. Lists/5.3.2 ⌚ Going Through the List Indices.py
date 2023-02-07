"""Create a program that first reads 5 numbers a user has entered and then prints all the entered numbers in reverse
order """


def main():
    a = [0, 0, 0, 0, 0]
    print("Give 5 numbers:")
    for i in range(0, 5):
        a[i] = int(input("Next number: "))
    print("The numbers you entered, in reverse order:")
    for i in range(len(a)-1, -1, -1):
        print(a[i])


if __name__ == "__main__":
    main()
