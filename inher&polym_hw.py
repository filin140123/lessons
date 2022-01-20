class GameCharacter:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def speak(self):
        print(f"Hi, my name is {self.name}")


class Villain(GameCharacter):
    def __init__(self, name, health, level):
        GameCharacter.__init__(self, name, health, level)

    def speak(self):
        print(f"Hi, my name is {self.name} and I will kill you")

    @staticmethod
    def kill(target: GameCharacter):
        target.health = 0
        print("Bang-bang, now you're dead")
