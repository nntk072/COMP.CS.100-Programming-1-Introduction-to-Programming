"""
Player 1, enter your choice (R/P/S): P
Player 2, enter your choice (R/P/S): S
Player 2 won!
s>p
s<r
r>s and r<p
"""


def main():
    a = input("Player 1, enter your choice (R/P/S): ")
    b = input("Player 2, enter your choice (R/P/S): ")
    if (a == "R" and b == "S") or (a == "P" and b == "R") or (a == "S" and b == "P"):
        print("Player 1 won!")
    elif a == b:
        print("It's a tie!")
    elif (b == "R" and a == "S") or (b == "P" and a == "R") or (b == "S" and a == "P"):
        print("Player 2 won!")


if __name__ == "__main__":
    main()
