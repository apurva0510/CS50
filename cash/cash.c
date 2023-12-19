#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}

int get_cents(void)
{
    // TODO
    int change;
    do
    {
        change = get_int("Change owed: ");
    }
    while (change < 0);
    return change;
}

int calculate_quarters(int cents)
{
    // Calculate the number of quarters to give the customer
    int quarters;
    if (cents < 50 && cents > 24)
    {
        quarters = 1;
    }
    else if (cents < 75 && cents > 49)
    {
        quarters = 2;
    }
    else if (cents < 100 && cents > 74)
    {
        quarters = 3;
    }
    else
    {
        quarters = 0;
    }
    return quarters;
}

int calculate_dimes(int cents)
{
    // Calculate the number of dimes to give the customer
    int dimes;
    if (cents < 20 && cents > 9)
    {
        dimes = 1;
    }
    else if (cents < 25 && cents > 19)
    {
        dimes = 2;
    }
    else
    {
        dimes = 0;
    }
    return dimes;
}

int calculate_nickels(int cents)
{
    // Calculate the number of nickels to give the customer
    int nickels;
    if (cents < 10 && cents > 4)
    {
        nickels = 1;
    }
    else
    {
        nickels = 0;
    }
    return nickels;
}

int calculate_pennies(int cents)
{
    // Calculate the number of pennies to give the customer
    return cents;
}