"""Combine the previously implemented programs to create a program that asks the user if they're bored until they
are, and additionally requires them to answer with the letter "y", "Y", "n" or "N", ie. asks the user for the answer
repeatedly until receiving a valid input. """


def main():
    name = input("Bored? (y/n) ")
    a = 0
    while a < 1 :
        if name == "y" or name == "Y":
            print("Well, let's stop this, then.")
            a += 1
            break
        if name == "n" or name == "N":
            name = input("Bored? (y/n) ")
        else:
            print("Incorrect entry.")
            name = input("Bored? (y/n) ")


if __name__ == "__main__":
    main()
