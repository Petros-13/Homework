a = 3
b = 7
c = 9

print("Before swapping:")
print("a =", a, "b =", b, "c =", c)
a = a + b + c  
b = a - (b + c)  
c = a - (b + c)  
a = a - (b + c)  

print("\nAfter swapping:")
print("a =", a, "b =", b, "c =", c)
