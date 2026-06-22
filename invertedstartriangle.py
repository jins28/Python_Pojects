symbol = input("Enter the symbol : ")
rows = int(input("Enter the number of rows : "))
for row in range(1, rows+1):
    for col in range(row, rows+2):
        print(f"{symbol}", end='')
    print()
