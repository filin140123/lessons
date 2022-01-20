class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old"

    def __len__(self):
        return self.age

    def __add__(self, other):
        return self.age + other.age

    def __del__(self):
        print(f"Person object '{self.first_name}' has been deleted from memory")


jack = Person("Jack", "White", 45)
print(jack)
print(len(jack))

jane = Person("Jane", "Eyre", 30)
print(jack + jane)
