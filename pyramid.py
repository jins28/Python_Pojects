

symbol = input("enter your symbol :")
x = int(input("Enter number of rows :"))
for row in range(1, x+1):
    total_spaces = x - row
    sym = 2 * row - 1
    print(" " * total_spaces + symbol * sym)
