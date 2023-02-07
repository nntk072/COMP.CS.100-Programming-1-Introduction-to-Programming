"""
Create a program that reads a file and prints its contents with each row starts with the row's number and a space.
"""


def main():
    file_name = input("Enter the name of the score file: ")
    try:
        save_file = open(file_name, mode="r")
    except OSError:
        print(f"There was an error in reading the file.")
        return

    d = {}
    u = []
    a = 0
    for i in save_file:
        i = i.rstrip().split(' ')
        u.append(i)
        try:
            k = len(i)
            5 / (int(k) - 1)
        except:
            print("There was an erroneous line in the file:")
            print(f"{i[0]}")
            a = -100
            break
        try:
            int(i[1])
        except:
            print("There was an erroneous score in the file:")
            print(f"{i[1]}")
            a = -100
            break
    if -10 <= a <= 0:
        print("Contestant score:")
        for i in u:
            for t in range(0, len(i) - 1, 1):
                if i[t] in d:
                    d[i[t]] += int(i[1])
                else:
                    d[i[t]] = int(i[1])
        for i in sorted(d):
            print(f"{i} {d[i]}")


if __name__ == "__main__":
    main()
