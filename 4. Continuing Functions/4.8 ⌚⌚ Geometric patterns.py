"""
COMP.CS.100 Programming 1
Code template for geometric patterns.
"""

from math import pi


def function1resulta(a):
    """jfoiwejfiajewiofjaoejfaoiwej"""
    print(f"The circumference is {a * 4:.2f}")


def function1resultb(a):
    """jfoiwejfiajewiofjaoejfaoiwej"""
    print(f"The surface area is {a * a:.2f} ")


def function1():
    """
       Print a menu for user to select which geometric pattern to use in calculations.
    """
    a = float(input("Enter the length of the square's side: "))
    while a <= 0:
        a = float(input("Enter the length of the square's side: "))
    function1resulta(a)
    function1resultb(a)


def function2resulta(a, b):
    """jfoiwejfiajewiofjaoejfaoiwej"""
    print(f"The circumference is {(a + b) * 2:.2f}")


def function2resultb(a, b):
    """jfoiwejfiajewiofjaoejfaoiwej"""
    print(f"The surface area is {a * b:.2f}")


def function2():
    """
       Print a menu for user to select which geometric pattern to use in calculations.
    """
    a = float(input("Enter the length of the rectangle's side 1: "))
    while a <= 0:
        a = float(input("Enter the length of the rectangle's side 1: "))
    b = float(input("Enter the length of the rectangle's side 2: "))
    while b <= 0:
        b = float(input("Enter the length of the rectangle's side 2: "))
    function2resulta(a, b)
    function2resultb(a, b)


def function3():
    """jfoiwejfiajewiofjaoejfaoiwej"""
    a = float(input("Enter the circle's radius: "))
    while a <= 0:
        a = float(input("Enter the circle's radius: "))
    print(f"The circumference is {a * pi * 2:.2f}")
    print(f"The surface area is {a * pi * a:.2f}")


def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            function1()  # Replace this comment and "pass" with your function calls dealing with square.
            pass

        elif answer == "r":
            function2()  # Replace this comment and "pass" with your function calls dealing with rectangle.
            pass

        elif answer == "c":
            function3()  # Replace this comment and "pass" with your function calls dealing with square.
            pass

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()


def main():
    """jfoiwejfiajewiofjaoejfaoiwej"""
    menu()
    print("Goodbye!")


if __name__ == "__main__":
    main()
