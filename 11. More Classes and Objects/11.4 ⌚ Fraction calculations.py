"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Fractions code template
"""


class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator
        self.numerator = numerator
        self.denominator = denominator

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator):.0f}/{abs(self.__denominator):.0f}"

    def simplify(self):
        for i in range(1, 1000, 1):
            if abs(self.__numerator) % i == 0 and abs(self.__denominator) % i == 0:
                self.__numerator = self.__numerator / i
                self.__denominator = self.__denominator / i

    def complement(self):
        complement = Fraction(-self.__numerator, self.__denominator)
        return complement

    def reciprocal(self):
        reciprocal = Fraction(self.__denominator, self.__numerator)
        return reciprocal

    def multiply(self, t):
        u = self.__numerator * t.numerator
        v = self.__denominator * t.denominator
        product = Fraction(u, v)

        return product

    def divide(self, t):
        u = int(self.__numerator * t.denominator)
        v = int(self.__denominator * t.numerator)
        quotinent = Fraction(u, v)
        return quotinent

    def add(self, t):
        u = int(self.__numerator * t.denominator + t.numerator * self.__denominator)
        v = int(self.__denominator * t.denominator)
        sum = Fraction(u, v)
        return sum

    def deduct(self, t):
        u = int(self.__numerator * t.denominator - t.numerator * self.__denominator)
        v = int(self.__denominator * t.denominator)
        different = Fraction(u, v)
        return different


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a


def main():
    object = Fraction(2, 4)
    result = object.complement()
    print(result.return_string())
    object = Fraction(2, -4)
    result = object.complement()
    print(result.return_string())
    object = Fraction(2, 4)
    result = object.reciprocal()
    print(result.return_string())
    object = Fraction(-2, -4)
    result = object.reciprocal()
    print(result.return_string())


if __name__ == "__main__":
    main()
