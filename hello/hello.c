#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Gets the user's name
    string name = get_string("What is your name?: ");

    // Prints the user's name
    printf("hello, %s\n", name);
    // printf("hello, world\n");
}