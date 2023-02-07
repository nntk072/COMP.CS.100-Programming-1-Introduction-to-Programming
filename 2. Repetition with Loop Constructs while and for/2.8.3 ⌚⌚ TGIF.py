"""
Create a program that prints the dates for all the Fridays in 2014. In 2014, the first Friday was 3.1.

Programming tips:

One possible solution is based on every seventh day being Friday. In the previous task, you implemented a program
that goes through all the dates of a year. You can add this program a counter whose value is always increased by one
when the program goes through the dates. The calculator can then be used to create a decision structure, which only
prints on every seventh date. Another solution is increasing the date in increments of seven and using a remainder
operator to select the right date when a month changes.
"""


def main():
    i = 3
    k = 1
    a = 2
    while a <= 2:
        while k == 1 and i <= 31:
            print(f"{i}.{k}.")
            i += 7
            if 31 - i == 0:
                print(f"{i}.{k}.")
                k += 1
                i = 7
                continue
            if 31 - i < 0:
                k += 1
                i = i - 31
                continue

        while k == 2 and i <= 28:
            print(f"{i}.{k}.")
            i += 7
            if 28 - i == 0:
                print(f"{i}.{k}.")
                k += 1
                i = 7
                continue
            if 28 - i < 0:
                k += 1
                i = i - 7 - 28
                if i <= 0:
                    i += 7
                continue
        while k == 3 or k == 5 or k == 7 or k == 8 or k == 10 or k == 12 and i <= 31:
            print(f"{i}.{k}.")
            i += 7
            if 31 - i == 0:
                print(f"{i}.{k}.")
                k += 1
                i = 7
                continue
            if 31 - i < 0:
                k += 1
                i = i - 31
                continue

        while k == 4 or k == 6 or k == 9 or k == 11 and i <= 30:
            print(f"{i}.{k}.")
            i += 7
            if 30 - i == 0:
                print(f"{i}.{k}.")
                k += 1
                i = -1
                continue
            if 30 - i < 0:
                k += 1
                i = i - 7 - 30
                continue
        if i <= 0:
            i += 7
        if k == 13:
            a += 1
            continue


if __name__ == "__main__":
    main()
