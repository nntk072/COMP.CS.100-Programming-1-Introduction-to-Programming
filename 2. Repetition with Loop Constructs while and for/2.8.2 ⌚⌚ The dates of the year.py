"""
Create a program that prints all the dates of a year which is not leap year:

1.1.
2.1.
3.1.
4.1.
5.1.
...
31.1.
1.2.
2.2.
3.2.
...
28.2.
1.3.
...
"""


def main():
    i = 1
    k = 1
    a = 2
    while a <=2:
        while k == 1 or k == 3 or k == 5 or k == 7 or k == 8 or k == 10 or k == 12 and i <= 31:
            print(f"{i}.{k}.")
            i += 1
            if i == 32:
                k += 1
                i = 1
                continue
        while k == 2 and i <= 28:
            print(f"{i}.{k}.")
            i += 1
            if i == 29:
                k += 1
                i = 1
                continue
        while k == 4 or k == 6 or k == 9 or k == 11 and i <= 30:
            print(f"{i}.{k}.")
            i += 1
            if i == 31:
                k += 1
                i = 1
                continue
        if k == 13:
            a +=1
            continue

if __name__ == "__main__":
    main()
