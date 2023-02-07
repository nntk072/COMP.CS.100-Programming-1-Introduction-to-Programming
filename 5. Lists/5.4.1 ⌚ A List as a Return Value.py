"""Create a function named input_to_list which has 1 parameter: number of integers user needs to enter. The function
then asks user to enter that many numbers, reads the numbers from the user, saves them in a list and returns that list.

Also create a main function which:

asks the user for the number of integers to be processed
calls input_to_list to read the numbers from the user
asks the user what number the user are searching for and
prints data on whether the searched numbers are found from the entered numbers and, if so, how many times
"""


def input_to_list(a):
    """joifjdsijfoiadjaoifj"""
    b = []
    for i in range(0, a):
        b.append(int(input()))
    return b


def main():
    """joifadsjoifjoisjfoiaew"""
    k = 0
    a = int(input('How many numbers do you want to process: '))
    print(f"Enter {a} numbers:")
    b = input_to_list(a)
    c = int(input("Enter the number to be searched: "))
    for i in range(0, len(b)):
        if c == b[i]:
            k += 1

    if k == 0:
        print(f"{c} is not among the numbers you have entered.")
    else:
        print(f"{c} shows up {k} times among the numbers you have entered.")


if __name__ == "__main__":
    main()
