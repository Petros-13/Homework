n = int(input())
if n < 0:
    n = -n
c = 1 if n == 0 else 0
while n:
    n //= 10
    c += 1
print(c)
