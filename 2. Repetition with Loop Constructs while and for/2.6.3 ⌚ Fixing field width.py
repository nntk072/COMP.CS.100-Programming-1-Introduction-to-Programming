"""
In other words, write it inside triple quotes like this
and place it right in the beginning of your program file.
Initial comment should explain who wrote the program and
what does it do.
"""


def main():
    for i in range(1, 11):
        for j in range(1, 11):
            a = int(i * j)
            if a < 10:
                print(f"   {i * j}", end="")
            elif 10 <= a <= 99:
                print(f"  {i * j}", end="")
            else:
                print(f" {i * j}", end="")
        print()


if __name__ == "__main__":
    main()
