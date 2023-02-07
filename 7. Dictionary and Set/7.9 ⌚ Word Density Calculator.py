"""Implement a word density calculator that reads a piece of text from the user and then prints how many times each
of the words appears in the text, """


def main():
    print("Enter rows of text for word counting. Empty row to quit.")
    b = []
    bien = 0
    while bien < 1:
        a = input()
        if a == "":
            bien = 1
        else:
            b.append(a)
    c = ' '.join(b)
    c = c.lower().split()
    d = {}
    for i in c:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in sorted(d):
        print(f"{i} : {d[i]} times")


if __name__ == "__main__":
    main()
