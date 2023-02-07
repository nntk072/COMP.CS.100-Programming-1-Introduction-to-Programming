"""
COMP.CS.100 Programming 1
Code template for  tourist dictionary.
"""


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    number = True
    while True:
        if number:
            print("Dictionary contents:")
            c = sorted(english_spanish)
            print(', '.join(c))
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":
            number = False
            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish.get(word)}")
            else:
                print("The word", word, "could not be found from the dictionary.")
        elif command == "A":
            number = True
            b = input("Give the word to be added in English: ")
            b1 = input("Give the word to be added in Spanish: ")
            english_spanish[b] = b1
        elif command == "R":
            number = False
            c = input("Give the word to be removed: ")
            if c in english_spanish:
                del english_spanish[c]
            else:
                print(f"The word {c} could not be found from the dictionary.")
        elif command == "P":
            number = False
            print()
            print("English-Spanish")
            for i in sorted(english_spanish):
                print(f"{i} {english_spanish[i]}")
            print("\nSpanish-English")
            spanish_english = dict((v, k) for k, v in english_spanish.items())
            for i in sorted(spanish_english):
                print(f"{i} {spanish_english[i]}")
            print()
        elif command == "T":
            d = input("Enter the text to be translated into Spanish: ")
            k = d.split()
            for i in range(0, len(k)):
                if k[i] in english_spanish:
                    k[i] = english_spanish[k[i]]
            print("The text, translated by the dictionary:")
            print(' '.join(k))
        elif command == "Q":
            number = False
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


if __name__ == "__main__":
    main()
