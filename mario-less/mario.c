#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Asks user for height while rejecting values less than 1 and greater than 8
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height <= 0 || height > 8);

    // Prints the blocks
    for (int i = 0; i < height; i++)
    {
        // Prints spaces to right align
        if (height > 1)
        {
            for (int j = height; j > i + 1 ; j--)
            {
                printf(" ");
            }
        }

        // Prints hashes
        for (int k = 0; k <= i; k++)
        {
            printf("#");
        }

        printf("\n");
    }
}