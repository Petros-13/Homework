def implement_circuit(A, B, C):
    
    X = A & B          
    Y = B | C          
    Z = B & C         
    W = Y & Z        

    Q = X | W         

    return Q


A = int(input("Enter A (0 or 1): "))
B = int(input("Enter B (0 or 1): "))
C = int(input("Enter C (0 or 1): "))

output = implement_circuit(A, B, C)
print("Output Q:", output)
