"""
COMP.CS.100 Programming 1
Print a box with input error checking
"""


def read_input(a):
    """oifsjdoifjoiejfoijweoifjw"""
    try:
        k = int(input(a))
        while k <= 0:
            k = int(input(a))
            continue
    except ValueError:
        k = read_input(a)
    return k


def print_box(width, height, mark):
    """oifsjdoifjoiejfoijweoifjw"""
    for row_counter in range(1, int(height) + 1):
        for column_counter in range(1, int(width) + 1):
            print(mark, end="")
        print()


def main():
    """oifsjdoifjoiejfoijweoifjw"""
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
