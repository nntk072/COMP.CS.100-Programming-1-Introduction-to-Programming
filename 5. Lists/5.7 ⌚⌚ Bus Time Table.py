"""
COMP.CS.100 Programming 1
Code template for "replacing grades" program
"""


# TODO: add the definition for convert_grades here
def convert_grades(a, b):
    """idjfoiajdsfoijadsoifjaoiwjfoiejfaoiw"""
    t = 0
    c = True
    for i in range(0, len(b), 1):
        if c:
            if a <= b[i]:
                t = i
                c = False
    print(b[t])
    if t + 1 == 6:
        print(b[0])
    else:
        print(b[t + 1])
    if t + 2 == 6:
        print(b[0])
    elif t + 2 == 7:
        print(b[1])
    else:
        print(b[t + 2])


def main():
    """idjfoiajdsfoijadsoifjaoiwjfoiejfaoiw"""
    grades = [630, 1015, 1415, 1620, 1720, 2000]
    a = int(input("Enter the time (as an integer): "))
    print("The next buses leave:")
    convert_grades(a, grades)


if __name__ == "__main__":
    main()
