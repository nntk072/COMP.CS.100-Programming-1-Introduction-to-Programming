"""Create a function named input_to_list which has 1 parameter: number of integers user needs to enter. The function
then asks user to enter that many numbers, reads the numbers from the user, saves them in a list and returns that list.

Also create a main function which:

asks the user for the number of integers to be processed
calls input_to_list to read the numbers from the user
asks the user what number the user are searching for and
prints data on whether the searched numbers are found from the entered numbers and, if so, how many times
"""


# from numpy import mean


def main():
    """joifadsjoifjoisjfoiaew"""
    b = []
    t = 0
    for i in range(0, 5, 1):
        b.append(float(input(f'Enter the time for performance {i + 1}: ')))
    b.remove(max(b))
    b.remove(min(b))
    # c = mean(b)
    for i in range(0, len(b)):
        t = t + b[i]
    t = t / len(b)
    print(f"The official competition score is {t:.2f} seconds.")
    # print(f"The official competition score is {c:.2f} seconds.")


if __name__ == "__main__":
    main()
