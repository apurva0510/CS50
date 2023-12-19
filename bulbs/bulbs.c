#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    string text = get_string("Text: ");
    int length = strlen(text);

    for (int i = 0; i < length; i++)
    {
        int byte[8];
        // Finds remainder and divides by 2
        for (int j = 0; j < 8; j++)
        {
            byte[j] = text[i] % 2;
            text[i] /= 2;
        }
        // Calls print bulb function
        for (int k = 7; k >= 0; k--)
        {
            print_bulb(byte[k]);
        }
        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
