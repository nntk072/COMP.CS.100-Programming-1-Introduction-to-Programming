"""
In other words, write it inside triple quotes like this
and place it right in the beginning of your program file.
Initial comment should explain who wrote the program and
what does it do.
"""


def main():
    number = input("Choose a number: ")
    i = 1
    number = int(number)
    while i <= 10:
        a = i * number
        print(i, '*', number,'=', a)
        i += 1


if __name__ == "__main__":
    main()
