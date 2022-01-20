class Swimmable:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"Hello, my name is {self.name} and I can swim")

    def swim(self):
        print("I'm swimming...")


class Walkable:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"Hello, my name is {self.name} and I can walk")

    def walk(self):
        print("I'm walking...")


class Flyable:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"Hello, my name is {self.name} and I can fly")

    def fly(self):
        print("I'm flying...")


class GameCharacter(Swimmable, Walkable, Flyable):
    def __init__(self, name):
        self.name = name
        Swimmable.__init__(self, name)
        Walkable.__init__(self, name)
        Flyable.__init__(self, name)

    def greeting(self):
        print(f"Hello, my name is {self.name}")


james = GameCharacter("James")
james.greeting()
james.swim()
james.walk()
james.fly()
print(isinstance(james, Swimmable), isinstance(james, Walkable), isinstance(james, Flyable))
print(isinstance(james, GameCharacter))
print(isinstance(james, object))
