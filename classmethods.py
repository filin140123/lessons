class Car:

    wheels_number = 4

    def __init__(self, name: str, color: str, year: int, is_crashed: bool):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed

    def driving_to(self, city: str):
        print(self.name + " is goes to " + city)

    def change_color(self, new_color):
        self.color = new_color


opel_car = Car("Opel Tigra", "grey", 1999, True)
opel_car.driving_to("London")

opel_car.change_color("red")
print(opel_car.color)
