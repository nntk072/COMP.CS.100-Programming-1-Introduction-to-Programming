"""Create a program that prints a multiplication table for a given number until it reaches a result that is more than
hundred. """


def main():
    number = input("Choose a number: ")
    a = i = 1
    number = int(number)
    while a <= 100:
        a = i * number
        print(i, '*', number, '=', a)
        i += 1


if __name__ == "__main__":
    main()
