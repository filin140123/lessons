class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Class successor must implement this method")


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def speak(self):
        print(f"{self.name} is saying woof")


class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def speak(self):
        print(f"{self.name} is saying meow")


class Mouse(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def speak(self):
        print(f"{self.name} is saying peep")


class Fish(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)


spike = Dog("Spike")
tom = Cat("Tom")
jerry = Mouse("Jerry")
freddy = Fish("Freddy")

pet_list = [spike, tom, jerry, freddy]

for pet in pet_list:
    pet.speak()
