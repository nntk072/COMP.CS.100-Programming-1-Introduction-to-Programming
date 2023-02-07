"""In various lists of names, names are sometimes presented in reverse order, the last name before the first name,
so that there is a comma after the last name. Create a function reverse_name, which changes a string containing such
a name to the order, where the first name is followed with the last name. The names are separated with a space and
the comma as well as all unnecessary spaces are removed. The function returns the modified name.

It is assumed that the name string contains no more than one comma and that the caller of the function always passes
at least one character as a parameter value (an empty string "" cannot be a parameter value). """


def reverse_name(a):
    """jfdsijfojsdofisdjfoisdjfoi"""
    b = a.split(",")
    print(b)
    c = []
    for i in range(len(b)-1, -1, -1):
        if b[i].strip() != "":
            c.append(b[i].strip())
    k = ' '.join(c)
    return k


def main():
    """jfdsijfojsdofisdjfoisdjfoi"""
    a = input()
    reverse_name(a)


if __name__ == "__main__":
    main()
