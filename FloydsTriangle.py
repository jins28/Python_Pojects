rows = int(input("Enter the number of rows :"))
num = 1
for row in range(1, rows+1):
    for col in range(0, row):
        print(num, end=" ")
        num += 1
    print()
