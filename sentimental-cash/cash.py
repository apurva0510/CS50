from cs50 import get_float


def main():
    # Ask how many cents the customer is owed
    cents = get_cents()

    # Calculate the number of quarters to give the customer
    quarters = calculate_quarters(cents)
    cents -= quarters * 25

    # Calculate the number of dimes to give the customer
    dimes = calculate_dimes(cents)
    cents -= dimes * 10

    # Calculate the number of nickels to give the customer
    nickels = calculate_nickels(cents)
    cents -= nickels * 5

    # Calculate the number of pennies to give the customer
    pennies = calculate_pennies(cents)
    cents -= pennies * 1

    # Sum coins
    coins = quarters + dimes + nickels + pennies

    # Print total number of coins to give the customer
    print(coins)


def get_cents():
    # TODO
    while True:
        change = get_float("Change owed: ")
        if change >= 0:
            break
    return int(change * 100)


def calculate_quarters(cents):
    # Calculate the number of quarters to give the customer
    quarters = 0
    if 25 <= cents < 50:
        quarters = 1
    elif 50 <= cents < 75:
        quarters = 2
    elif cents >= 75:
        quarters = 3
    return quarters


def calculate_dimes(cents):
    # Calculate the number of dimes to give the customer
    dimes = 0
    if 10 <= cents < 20:
        dimes = 1
    elif cents >= 20:
        dimes = 2
    return dimes


def calculate_nickels(cents):
    # Calculate the number of nickels to give the customer
    nickels = 0
    if 5 <= cents < 10:
        nickels = 1
    return nickels


def calculate_pennies(cents):
    # Calculate the number of pennies to give the customer
    return cents


if __name__ == "__main__":
    main()