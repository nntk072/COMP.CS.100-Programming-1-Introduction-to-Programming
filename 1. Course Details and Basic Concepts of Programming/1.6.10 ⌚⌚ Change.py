"""
Create a program that asks how much purchases cost and the amount of paid money and then prints the amount of change.
Simplify the program by only allowing the use of sums of 1, 2, 5 and 10 euros.
Ensure that the total price is always in full euros.
Purchase price: 12
Paid amount of money: 50
Offer change:
3 ten-euro notes
1 five-euro notes
1 two-euro coins
1 one-euro coins

"""


def main():
    a = b = c = i = m = n = p = 0
    a = input("Purchase price: ")
    b = input("Paid amount of money: ")
    a = int(a)
    b = int(b)
    c = b - a
    # calculator
    if c < 0:
        print("No change")
    if c == 0:
        print("No change")
    if c > 0:
        print("Offer change:")
        while c >= 10 and c // 10 > 0:
            i = i + 1
            c = c - 10

        while 10 > c >= 5 and c // 5 > 0:
            m = m + 1
            c = c - 5

        while 5 > c >= 2 and c // 2 > 0:
            n = n + 1
            c = c - 2

        while 2 >= c >= 1:
            p = p + 1
            c = c - 1

    # The results

    if i > 0:
        print(i, "ten-euro notes")
    if m > 0:
        print(m, "five-euro notes")
    if n > 0:
        print(n, "two-euro coins")
    if p > 0:
        print(p, "one-euro coins")


if __name__ == "__main__":
    main()
