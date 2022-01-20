class Car:

    wheels_number = 4

    def __init__(self, name: str, color: str, year: int, is_crashed: bool):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed
        print("Car is created")

    def driving_to(self, city: str):
        print(self.name + " is goes to " + city)

    def change_color(self, new_color):
        self.color = new_color
        print(f"Color is changed to {new_color}")


class Truck(Car):
    wheels_number = 6
    cargo = 0

    def __init__(self, name: str, color: str, year: int, is_crashed: bool):
        Car.__init__(self, name, color, year, is_crashed)
        print("Truck is created")

    def driving_to(self, city: str):
        print(f"Truck {self.name} is goes to {city}")

    def load_cargo(self, weight):
        Truck.cargo += weight
        print(f"Cargo is loaded. Weight is {weight} kg")


man_truck = Truck("MAN", "white", 2020, False)
man_truck.driving_to("New York")
man_truck.change_color("black")
print(man_truck.wheels_number)
man_truck.load_cargo(500)
print(man_truck.cargo)
