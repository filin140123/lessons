class Gamer:
    active_gamers = 0

    @classmethod
    def get_active_gamers(cls):
        return Gamer.active_gamers

    @classmethod
    def gamer_from_string(cls, data_string):
        nickname, age, level, points = data_string.split(',')
        return cls(nickname, age, level, points)

    def __init__(self, nickname, age, level, points):
        self.nickname = nickname
        self.age = age
        self.level = level
        self.points = points
        Gamer.active_gamers += 1

    def logout(self):
        Gamer.active_gamers -= 1

    def get_nickname(self):
        return self.nickname

    def get_age(self):
        return self.age

    def get_level(self):
        return self.level

    def get_points(self):
        return self.points

    def is_adult(self):
        return self.age >= 18

    def get_adult_level_permission(self):
        if self.is_adult():
            print("You can enter to adult level")
        else:
            print("Sorry, you can't enter to adult level")


gamer1 = Gamer("hellboy", 23, 5, 13)
gamer2 = Gamer("harry", 13, 7, 34)

print(gamer1.get_age())
gamer1.get_adult_level_permission()

print(gamer2.get_age())
gamer2.get_adult_level_permission()

print(Gamer.get_active_gamers())

james = Gamer.gamer_from_string("James,34,2,45")
jane = Gamer.gamer_from_string("Jane,24,5,61")

mydict = dict.fromkeys((1,2,3), ("apple","orange","banana"))
print(mydict)
