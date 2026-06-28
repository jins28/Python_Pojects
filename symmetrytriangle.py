x = int(input("Enter the number of rows : "))
for row in range(1, x+1):
    total_space = x-row
    print(" "*total_space, end="")
    for col in range(1, row+1):

        print(col, end=" ")
    print()
