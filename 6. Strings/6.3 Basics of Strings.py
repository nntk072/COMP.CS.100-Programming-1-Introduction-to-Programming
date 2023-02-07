"""
Write a program that asks from a user an English word and tells how many vowels and consonants the word contains.
The vowels of the English language are represented in the English lower-case alphabet with letters a, e, i,
o and u. In this task, the lower-case y letter is considered a symbol of a vowel, although it can represent also a
consonant sound in English.
"""


def main():
    """jfdsijfojsdofisdjfoisdjfoi"""
    word = input("Enter a word: ")
    a = 0
    b = 0
    for i in range(0, len(word)):
        if word[i] == "a" or word[i] == "e" or word[i] == "o" or word[i] == "u" or word[i] == "i" or word[i] == "y":
            a += 1
        else:
            b += 1
    print(f"The word \"{word}\" contains {a} vowels and {b} consonants.", end="")


if __name__ == "__main__":
    main()
