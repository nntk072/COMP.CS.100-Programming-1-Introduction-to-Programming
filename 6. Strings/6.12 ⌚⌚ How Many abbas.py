"""Implement the function count_abbas, which returns the number of abbas (meaning the string "abba") that the
parameter string contains. """


def count_abbas(a):
    """jfdoisjfoisdjfiosdjifo"""
    c = 0
    for i in range(0, len(a), 1):
        if len(a) - i >= 4:
            if a[i:i + 4] == "abba":
                c += 1
    return c


def main():
    """fjoiewjfoiewjfoiew"""
    a = input()
    count_abbas(a)


if __name__ == "__main__":
    main()
