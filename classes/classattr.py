class Car:

    wheels_number = 4

    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed


mazda_car = Car(name="Mazda CX7", color="red", year=2017, is_crashed=True)
print(mazda_car.name, mazda_car.color, mazda_car.year, sep=", ")

bmw_car = Car(name="BMW M5", color="black", year=2018, is_crashed=False)
print(bmw_car.name, bmw_car.is_crashed, bmw_car.wheels_number, sep=", ")

number_of_wheels_of_three_cars = Car.wheels_number * 3
print(number_of_wheels_of_three_cars)
