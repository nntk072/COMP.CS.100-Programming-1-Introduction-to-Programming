"""
COMP.CS.100 Programming 1
Code template for "replacing grades" program
"""


# TODO: add the definition for convert_grades here
def convert_grades(a):
    """idjfoiajdsfoijadsoifjaoiwjfoiejfaoiw"""
    for i in range(0, len(a), 1):
        if a[i] > 0:
            a[i] = 6


def main():
    """idjfoiajdsfoijadsoifjaoiwjfoiejfaoiw"""
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()
