num = int(input("Enter a number: "))
n = int(input("Enter how many powers to show: "))

for i in range(1, n + 1):
    print(num, "^", i, "=", num ** i)
