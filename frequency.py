test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

print("Test Dictionary:", test_dict)

word = input("Enter the word to check its frequency: ")

if word in test_dict:
    print(f"The frequency of '{word}' is:", test_dict[word])
else:
    print(f"'{word}' is not in the dictionary.")
