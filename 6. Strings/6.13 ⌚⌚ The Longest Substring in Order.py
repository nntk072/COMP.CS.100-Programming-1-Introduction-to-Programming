"""Implement the function count_abbas, which returns the number of abbas (meaning the string "abba") that the
parameter string contains. """


def longest_substring_in_order(a):
    """jfdoisjfoisdjfiosdjifo"""
    r = ''
    c = ''
    for i in a:
        if c == '':
            c = i
        elif c[-1] <= i:
            c += i
        elif c[-1] > i:
            if len(r) < len(c):
                r = c
                c = i
            else:
                c = i
    if len(c) > len(r):
        r = c
    return r


def main():
    """fjoiewjfoiewjfoiew"""
    a = input()
    longest_substring_in_order(a)


if __name__ == "__main__":
    main()
