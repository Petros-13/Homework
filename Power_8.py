n = int(input())
if n > 0 and (n & (n - 1)) == 0 and (n.bit_length() - 1) % 3 == 0:
    print("Yes")
else:
    print("No")
