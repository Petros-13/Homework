total_bill = float(input("Enter the total bill amount: $"))
amount_paid = float(input("Enter the amount paid: $"))
change = amount_paid - total_bill
print(f"The shopkeeper should return: ${change:.2f}")
