#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string word = get_string("Word: ");

    int word_length = strlen(word);
    for (int i = 0; i < word_length - 1; i++)
    {
        // Check if NOT alphabetical (i.e., "ha")
        if (word[i] > word[i + 1])
        {
            printf("No\n");
            return 0;
        }
    }

    printf ("Yes\n");
    return 0;
}