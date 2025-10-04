class Dog:
    animal = "dog"

    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

dog1 = Dog("Labrador", "Black")
dog2 = Dog("Poodle", "White")

print(f"Dog 1 is a {dog1.animal}. Breed: {dog1.breed}, Colour: {dog1.colour}")
print(f"Dog 2 is a {dog2.animal}. Breed: {dog2.breed}, Colour: {dog2.colour}")
