import string
import math


def main():
    # Gets user input for text
    text = input("Text: ")

    # Computes the number of letters in the text
    letters = count_letters(text)

    # Computes the number of words in the text
    words = count_words(text)

    # Computes the number of sentences in the text
    sentences = count_sentences(text)

    # Defining Coleman-Liau index

    # L is the average number of letters per 100 words in the text
    L = (letters / words) * 100

    # S is the average number of sentences per 100 words in the text.
    S = (sentences / words) * 100

    index = round(0.0588 * L - 0.296 * S - 15.8)

    if index < 1:
        print("Before Grade 1")
    elif index > 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


def count_letters(text):
    # Computes the number of letters in the text
    act_length = sum(1 for char in text if char.isalpha())
    return act_length


def count_words(text):
    # Computes the number of words in the text
    words = len(text.split())
    return words


def count_sentences(text):
    # Computes the number of sentences in the text
    sentences = 0
    for char in text:
        if char in ['.', '!', '?']:
            sentences += 1
    return sentences


if __name__ == "__main__":
    main()