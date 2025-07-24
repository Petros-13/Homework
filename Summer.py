hot = 45
warm = 35
cold = 12

temperature = int(input("Enter the temperature: "))

if temperature >= hot:
    print("It's hot, put on a shirt and shorts.")
elif temperature >= warm:
    print("It's warm, put on a shirt and short sleeves.")
elif temperature >= cold:
    print("It's cold, wear a jacket and long pants.")
else:
    print("It's very cold, bundle up!")
