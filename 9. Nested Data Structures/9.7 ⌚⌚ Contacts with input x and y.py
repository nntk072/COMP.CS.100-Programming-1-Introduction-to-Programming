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
    k = []
    info = {}
    x = input()
    y = input()
    a = ""
    file = open(filename, mode="r")
    for row in file:
        a = row.rstrip().split(";")
        k.append(a)
    print(k)
    for i in range(0, len(k[0]), 1):
        info[k[0][i]] = []

    for i in range(1, len(k), 1):
        for t in range(0, len(k[0]), 1):
            info[k[0][t]].append(k[i][t])
    t = 0
    if x in info[k[0][0]]:
        u = int(info[k[0][0]].index(x))

        if y in k[0]:
            t = int(k[0].index(y))
        a = info[k[0][t]][u]
    return a


def main():
    filename = input("")

    info = read_file(filename)


if __name__ == "__main__":
    main()
