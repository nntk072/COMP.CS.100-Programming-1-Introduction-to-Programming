"""
COMP.CS.100 Programming 1
Read genres and tv-series from a file into a dict.
Print a list of the genres in alphabetical order
and list tv-series by given genre on user's command.
"""


# genre_list:
# genre

def read_file(filename):
    """
    Reads and saves the series and their genres from the file.
    TODO: comment the parameter and the return value.
    :parameter filename:string
    :return data: info
    """
    file = open(filename, mode="r")
    info = {}
    k = []
    for row in file:
        a = row.rstrip().split(";")
        k.append(a)

    for i in range(1, len(k), 1):
        listtodictionary = {}
        for t in range(1, len(k[0]), 1):
            listtodictionary[k[0][t]] = k[i][t]
        info[k[i][0]] = listtodictionary
    return info


def main():
    filename = input("")
    info = read_file(filename)
    print(info)

if __name__ == "__main__":
    main()
