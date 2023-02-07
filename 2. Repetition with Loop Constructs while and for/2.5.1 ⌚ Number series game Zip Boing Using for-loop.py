"""
In other words, write it inside triple quotes like this
and place it right in the beginning of your program file.
Initial comment should explain who wrote the program and
what does it do.
"""


def main():
    number = input("How many numbers would you like to have? ")
    i = 1
    number = int(number)
    for i in range(1, number + 1):
        if i % 21 == 0:
            print("zip boing")

        elif i % 7 == 0:
            print("boing")
        elif i % 3 == 0:
            print("zip")
        else:
            print(i)
        i += 1


if __name__ == "__main__":
    main()
