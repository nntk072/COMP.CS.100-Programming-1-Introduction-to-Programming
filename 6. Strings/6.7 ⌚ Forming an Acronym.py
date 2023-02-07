"""In various lists of names, names are sometimes presented in reverse order, the last name before the first name,
so that there is a comma after the last name. Create a function reverse_name, which changes a string containing such
a name to the order, where the first name is followed with the last name. The names are separated with a space and
the comma as well as all unnecessary spaces are removed. The function returns the modified name.

It is assumed that the name string contains no more than one comma and that the caller of the function always passes
at least one character as a parameter value (an empty string "" cannot be a parameter value). """


def create_an_acronym(a):
    """jfoidsjfoisdjfoidsjfoij"""
    b = a[0]
    for i in range(1, len(a)):
        if a[i - 1] == ' ':
            b += a[i]
    b = b.upper()
    return b


def main():
    """jfdsijfojsdofisdjfoisdjfoi"""
    a = input()
    create_an_acronym(a)


if __name__ == "__main__":
    main()
