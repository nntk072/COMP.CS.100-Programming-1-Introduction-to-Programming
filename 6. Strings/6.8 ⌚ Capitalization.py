"""Create the function capitalize_initial_letters, which uses a string as a parameter and returns it as written,
with each word starting in upper case but the rest of the world in lower case. """


def capitalize_initial_letters(a):
    """jfoisdjfoisdjfiodsjfoisjdoifjsdoi"""
    c = ""
    list_of_words = a.split()
    for i in list_of_words:
        if len(c) > 0:
            c = c + " " + i.strip().capitalize()
        else:
            c = i.capitalize()
    if not c:
        return a
    else:
        return c


def main():
    """jfoisdjfoisdjfiodsjfoisjdoifjsdoi"""
    a = input()
    capitalize_initial_letters(a)


if __name__ == "__main__":
    main()
