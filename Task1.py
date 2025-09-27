num = int(input("Enter a number: "))

odd_numbers_below = [x for x in range(num) if x % 2 != 0]
odd_numbers_up_to = [x for x in range(1, num+1) if x % 2 != 0]

print("Odd numbers below the input:", odd_numbers_below)
print("Odd numbers up to the input:", odd_numbers_up_to)

fruits = ['apple', 'banana', 'cherry', 'mango', 'orange']
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Capitalized fruits list:", capitalized_fruits)
