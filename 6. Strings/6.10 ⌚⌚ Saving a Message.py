"""
COMP.CS.100 Programming 1
Code Template
"""


def read_message():
    """fjoidjfojeowijowejfiowe"""
    b = []
    bien = 0
    while bien < 1:
        a = input()
        if a == "":
            bien = 1
        else:
            b.append(a)
    return b


def main():
    """jfoisdjfoijoiewjfew"""
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()
    for i in range(0, len(msg), 1):
        msg[i] = msg[i].upper()
    print("The same, shouting:")
    print('\n'.join(msg))


if __name__ == "__main__":
    main()
