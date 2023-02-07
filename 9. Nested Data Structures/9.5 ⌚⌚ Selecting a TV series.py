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
    :return data: dictionary
    """

    # TODO initialize a new data structure
    dictionaryforfilm = {}
    listfortypeoffilm = []

    try:
        file = open(filename, mode="r")
        for row in file:
            # If the input row was correct, it contained two parts:
            # · the show name before semicolon (;) and
            # · comma separated list of genres after the semicolon.
            # If we know that a function (method split in this case)
            # returns a list containing two elements, we can assign
            # names for those elements as follows:
            name, genres = row.rstrip().split(";")
            genres = genres.split(",")
            for i in genres:
                if i not in listfortypeoffilm:
                    listfortypeoffilm.append(i)

                try:
                    if name not in dictionaryforfilm[i]:
                        dictionaryforfilm[i].append(name)
                except:
                    dictionaryforfilm[i] = list()
                    if name not in dictionaryforfilm[i]:
                        dictionaryforfilm[i].append(name)
        # TODO add the name and genres data to the data structure

        file.close()
        return dictionaryforfilm, listfortypeoffilm  # TODO return the data structure

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None
    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")
    genre_data, filmlist = read_file(filename)
    filmlist = sorted(filmlist)
    Availablegenres = ", ".join(filmlist)
    # TODO print the genres
    print(f"Available genres are: {Availablegenres}")
    while True:
        k = []
        genre = input("> ")
        if genre == "exit":
            return
        try:
            for i in genre_data[genre]:
                k.append(i)
            k.sort()
            for i in k:
                print(i)
        except:
            continue
        # TODO print the series belonging to a genre.


if __name__ == "__main__":
    main()
