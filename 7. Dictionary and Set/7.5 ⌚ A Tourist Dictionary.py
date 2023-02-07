"""
COMP.CS.100 Programming 1
Code template for  tourist dictionary.
"""


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish.get(word)}")
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            b = input("Give the word to be added in English: ")
            b1 = input("Give the word to be added in Spanish: ")
            english_spanish[b] = b1
        elif command == "R":
            c = input("Give the word to be removed: ")
            if c in english_spanish:
                del english_spanish[c]
            else:
                print(f"The word {c} could not be found from the dictionary.")
        elif command == "P":
            for i in sorted(english_spanish):
                print(f"{i} {english_spanish[i]}")
        elif command == "T":
            d = input("Enter the text to be translated into Spanish: ")
            k = d.split()
            for i in range(0, len(k)):
                if k[i] in english_spanish:
                    k[i] = english_spanish[k[i]]
            print("The text, translated by the dictionary:")
            print(' '.join(k))
        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


if __name__ == "__main__":
    main()
