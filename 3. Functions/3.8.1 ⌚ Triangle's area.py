"""
Ohjelmointi 1 / Programming 1
Trangle's Area when the Sides Are Known
"""
from math import sqrt

"""fiajoiwejfoiawjefoiew"""


def area(a, b, c):
    """fjoaidjfioawejoifjwaeoifjaewoifja"""
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))


"""fjoiawejfoiewjfoiawjeiojwoef"""


def main():
    """jwoiejfoiawjfoiaejfoiawejoijf"""
    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))
    print(f"The triangle's area is {area(a, b, c):.1f}")


if __name__ == "__main__":
    main()
