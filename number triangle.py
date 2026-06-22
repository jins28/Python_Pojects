num = int(input("Enter the limit : "))
rows = int(input("Enter the number of rows : "))
for row in range(1, rows+1):
    for col in range(1, row+1):

        print(f"{col}", end='')
    print()
