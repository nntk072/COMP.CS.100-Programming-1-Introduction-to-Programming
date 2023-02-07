"""The program you implemented in the previous section will not work properly when the user enters something other
than "y", "Y", "n", or "N". Now, implement a whole new program, which only contains a repeating structure that asks
the user's answer again if the answer is not "y", "Y", "n" or "N". """


def main():
    name = input("Answer Y or N: ")
    a = True
    while a:
        if name == "n" or name == "N" or name == "y" or name == "Y":
            print("You answered", name)
            return
        if name != "n" or name != "N" or name != "y" or name != "Y":
            print("Incorrect entry.")
            name = input("Answer Y or N: ")


if __name__ == "__main__":
    main()
