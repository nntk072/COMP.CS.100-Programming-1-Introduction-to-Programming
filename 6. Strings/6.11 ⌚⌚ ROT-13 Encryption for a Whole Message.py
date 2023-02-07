"""
COMP.CS.100 Programming 1
ROT13 program code template
"""


def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.
    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """
    regular_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                     "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                     "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]
    # TODO: implement encryption here
    first = ''.join(regular_chars)
    second = ''.join(encrypted_chars)
    k = []
    for i in text:
        k.append(i)
    c = []
    for i in range(0, len(k), 1):
        if k[i].islower():
            t = first.find(k[i])
            c.append(second[t])
        elif k[i].isupper():
            u = k[i].lower()
            t = first.find(u)
            c.append(second[t].upper())
        else:
            c.append(k[i])
    d = ''.join(c)
    return d


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


def row_encryption(c):
    """fjisdjfoisdjfiojweoijfewfoiewjf"""
    d = encrypt(c)
    return d


def main():
    """jfoijfoiewjfoiwejoifjewioj"""
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()
    print("ROT13:")
    hahaha = '\n'.join(msg)
    kakaka = row_encryption(hahaha)
    print(kakaka)


if __name__ == "__main__":
    main()
