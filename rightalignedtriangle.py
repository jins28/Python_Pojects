symbol = input("Enter the symbol : ")
rows = int(input("Enter the number of rows: "))
for row in range(1, rows+1):
    total_spaces = (rows-row)
    print(total_spaces * " " + symbol*row)
