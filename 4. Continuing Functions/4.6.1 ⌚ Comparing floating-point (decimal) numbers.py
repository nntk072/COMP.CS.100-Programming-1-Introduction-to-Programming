"""Implement the function compare_floats that uses two floating point numbers and an epsilon as a parameter and
returns information on whether the numbers are same to a sufficient degree (the parameter epsilon) as a truth value. """


def compare_floats(a, b, c):
    """jfoajewoifjwoiefjoiawejfo"""
    k = True
    if abs(a - b) < c:
        k = True
    else:
        k = False
    return k


def main():
    """jfoajewoifjwoiefjoiawejfo"""
    EPSILON = float(input())
    a = float(input())
    b = float(input())
    compare_floats(a, b, EPSILON)


if __name__ == "__main__":
    main()
