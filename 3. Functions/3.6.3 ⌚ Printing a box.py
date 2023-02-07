"""
COMP.CS.100 Programming 1
Template for task: box printing
"""


def print_box(width, height, mark):
    """oifsjdoifjoiejfoijweoifjw"""
    for row_counter in range(1, int(height) + 1):
        for column_counter in range(1, int(width) + 1):
            print(mark, end="")
        print()


"""oifsjdoifjoiejfoijweoifjw"""


def main():
    """oifsjdoifjoiejfoijweoifjw"""
    width = input("Enter the width of a frame: ")
    height = input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
