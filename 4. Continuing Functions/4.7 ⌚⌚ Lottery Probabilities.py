"""Implement the function compare_floats that uses two floating point numbers and an epsilon as a parameter and
returns information on whether the numbers are same to a sufficient degree (the parameter epsilon) as a truth value. """


def function1(a, b):
    """jfoajewoifjwoiefjoiawejfo"""
    x = y = z = 1
    t = a - b
    c = 0
    if a > 0:
        if t > 0:
            for i in range(1, a + 1):
                x = x * i
            for i in range(1, t + 1):
                y = y * i
            for i in range(1, b + 1):
                z = z * i
            print(x)
            print(y)
            print(z)
            c = x / (y * z)
    return c


def function2(a, b, c):
    """jfoajewoifjwoiefjoiawejfo"""
    t = a - b
    if a > 0:
        if t > 0:
            print(f"The probability of guessing all {b} balls correctly is 1/{c:.0f}")
        else:
            print(f"At most the total number of balls can be drawn.")
    else:
        print(f"The number of balls must be a positive number.")


def main():
    """jfoajewoifjwoiefjoiawejfo"""
    a = int(input("Enter the total number of lottery balls: "))
    b = int(input("Enter the number of the drawn balls: "))
    k = function1(a, b)
    function2(a, b, k)


if __name__ == "__main__":
    main()
