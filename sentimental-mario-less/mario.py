from cs50 import get_int

# Asks user for height while rejecting values less than 1 and greater than 8
while True:
    height = get_int("Height: ")
    if 0 < height <= 8:
        break

# Prints the blocks
for i in range(height):

    # Prints spaces to right align
    if height > 1:
        for j in range(height, i + 1, -1):
            print(" ", end="")

    # Prints hashes
    for k in range(i + 1):
        print("#", end="")

    print()