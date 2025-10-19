class BMW:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "240 km/h"


class Ferrari:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "340 km/h"


def car_details(car):
    print(f"Fuel Type: {car.fuel_type()}")
    print(f"Max Speed: {car.max_speed()}")
    print("---------------------------")


bmw_car = BMW()
ferrari_car = Ferrari()

car_details(bmw_car)
car_details(ferrari_car)
