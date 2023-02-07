"""
In other words, write it inside triple quotes like this
and place it right in the beginning of your program file.
Initial comment should explain who wrote the program and
what does it do.
"""


def main():
    name = int(input("How many Fibonacci numbers do you want? "))
    i = 1
    a = 1
    b = 1
    c = 0
    d = 0
    while i <= name:
        c = a + b
        d = a
        a = b
        b = c
        print(f"{i}. {d} ")
        i += 1


if __name__ == "__main__":
    main()
