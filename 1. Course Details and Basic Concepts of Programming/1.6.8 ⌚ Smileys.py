def main():
    haha = input("How do you feel? (1-10) ")
    if 7 < int(haha) < 10:
        print("A suitable smiley would be :-)")
    elif int(haha) == 1:
        print("A suitable smiley would be :'(")
    elif 4 <= int(haha) <= 7:
        print("A suitable smiley would be :-|")
    elif 0 < int(haha) < 4:
        print("A suitable smiley would be :-(")
    elif int(haha) == 10:
        print("A suitable smiley would be :-D")
    else:
        print("Bad input!")


if __name__ == "__main__":
    main()
