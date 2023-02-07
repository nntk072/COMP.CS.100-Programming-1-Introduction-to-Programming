"""
COMP.CS.100 Programming 1
Assignment "Improved Box Printing" code template
"""


# TODO: the definition of print_box goes here unless it goes after main.


def print_box(width, height, border_mark="#", inner_mark=" "):
    """jfoiwejfiajewiofjaoejfaoiwej"""
    for row_counter in range(1, height + 1):
        for column_counter in range(1, width + 1):
            if (row_counter == 1 or row_counter == height
                    or column_counter == 1 or column_counter == width):
                print(border_mark, end="")
            else:
                print(inner_mark, end="")
        print()


def main():
    """jfoiwejfiajewiofjaoejfaoiwej"""
    print_box(5, 4)
    print()
    print_box(3, 8, "*")
    print()
    print_box(5, 4, "O", "o")
    print()
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


# TODO: the definition of print_box could also go here, it is up to you.


if __name__ == "__main__":
    main()
