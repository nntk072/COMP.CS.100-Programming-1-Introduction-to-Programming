"""
Create a program that reads a file and prints its contents with each row starts with the row's number and a space.
"""


def main():
    file_name = input("Enter the name of the file: ")
    try:
        save_file = open(file_name, mode="w")
    except OSError:
        print(f"Writing the file {file_name} was not successful.")
        return
    print("Enter rows of text. Quit by entering an empty row.")
    k = 0
    t3 = -1
    while t3 < 0:
        text_line = input()
        if text_line == "":
            break
        if text_line.strip() != "":
            k += 1
            print(f"{k} {text_line}", file=save_file)
        else:
            t3 = 0
    save_file.close()
    print(f"File {file_name} has been written.")


if __name__ == "__main__":
    main()
