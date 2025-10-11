class Reverse:
    def __init__(self, s=""):
        self.s = s

    def get_reversed(self):
        return self.s[::-1]

user_input = input("Enter a word: ")
reverse_object = Reverse(user_input)
print("Reversed word:", reverse_object.get_reversed())
