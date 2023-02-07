"""Create the function are_all_members_same, which uses a list as a parameter and returns information on whether all
the members contained by the list are the same. """


def is_the_list_in_order(a):
    """Create the function are_all_members_same, which uses a list as a parameter and returns information on whether all
    the members contained by the list are the same. """

    c = True
    for i in range(0, len(a) - 1):
        if c:
            if a[i] <= a[i + 1]:
                c = True
            else:
                c = False
    return c


def main():
    """Create the function are_all_members_same, which uses a list as a parameter and returns information on whether all
    the members contained by the list are the same. """

    is_the_list_in_order([37, 42, 43])
    is_the_list_in_order([42, 37, 43])


if __name__ == "__main__":
    main()
