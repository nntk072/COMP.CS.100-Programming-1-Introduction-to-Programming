"""
In other words, write it inside triple quotes like this
and place it right in the beginning of your program file.
Initial comment should explain who wrote the program and
what does it do.
"""


def main():
    name = input("Bored? (y/n) ")
    while name == "n":
        name = input("Bored? (y/n) ")

    if name == "y":
        print("Well, let's stop this, then.")


if __name__ == "__main__":
    main()
