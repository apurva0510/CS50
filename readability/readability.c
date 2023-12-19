#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Gets user input for text
    string text = get_string("Text: ");

    // Computes the number of letters in the text
    float letters = count_letters(text);

    // Computes the number of words in the text
    float words = count_words(text);

    // Computes the number of sentences in the text
    float sentences = count_sentences(text);

    // Defining Coleman-Liau index

    // L is the average number of letters per 100 words in the text
    float L = letters / (words / 100);

    // S is the average number of sentences per 100 words in the text.
    float S = round(sentences / (words / 100));

    int index = round(0.0588 * L - 0.296 * S - 15.8);

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

int count_letters(string text)
{
    // Computes the number of letters in the text
    int length = strlen(text);
    int act_length = 0;

    for (int i = 0; i < length; i++)
    {
        if (isalpha(text[i]))
        {
            act_length++;
        }
    }
    return act_length;
}

int count_words(string text)
{
    // Computes the number of words in the text
    int words = 1;
    int length = strlen(text);

    for (int i = 0; i < length; i++)
    {
        if (text[i] == 32)
        {
            words++;
        }
    }
    return words;
}

int count_sentences(string text)
{
    // Computes the number of sentences in the text
    int sentences = 0;
    int length = strlen(text);

    for (int i = 0; i < length; i++)
    {
        if (text[i] == 33 || text[i] == 46 || text[i] == 77)
        {
            sentences++;
        }
    }
    return sentences;
}