def check_age():
    try:
        age_input = input("Enter your age: ")
        
        age = int(age_input)

        if age % 2 == 0:
            print(f"Age {age} is Even.")
        else:
            print(f"Age {age} is Odd.")

    except ValueError:
        print("Value Error: Please enter a valid integer age (no decimals, letters, or special characters).")
check_age()
