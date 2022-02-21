from random import randint


class Attack:
    def __init__(self, dmg, crit_chance, crit_coef, is_armor_piercing: bool):
        self.dmg = dmg
        self.crit_chance = crit_chance
        self.crit_coef = crit_coef
        self.is_armor_piercing = is_armor_piercing

    def attack(self, unit_health, unit_armor=0, unit_block_chance=0):
        """Returns health of unit after attack"""
        if 0 < unit_block_chance >= randint(1, 100):
            return unit_health

        if self.is_armor_piercing or unit_armor == 0:
            actual_damage = self.dmg
        else:
            actual_damage = self.dmg * (0.99 ** unit_armor)

        if self.crit_chance <= randint(1, 100):
            actual_damage *= self.crit_coef

        return unit_health - actual_damage


# # tests
# a = Attack(30, 25, 1.4, False)
#
# print("---")
# for i in range(100):
#     result = a.attack(100, 65, 50)
#     print(result)
#
# print("---")
# for i in range(100):
#     result = a.attack(100, 65)
#     print(result)
#
# print("---")
# for i in range(100):
#     result = a.attack(100)
#     print(result)
#
# print("---")
# for i in range(100):
#     result = a.attack(100, 10, 10)
#     print(result)
