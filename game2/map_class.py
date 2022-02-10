from random import randint
from prettytable import PrettyTable, DOUBLE_BORDER


class MapGenerator:
    __TOTAL_CHANCE = 100
    DIRECTIONS = ["up", "left", "right", "down"]

    @property
    def generate_tile(self):
        enemy_chance = randint(25, 50)
        treasure_chance = randint(5, 15)
        empty_chance = self.__TOTAL_CHANCE - (enemy_chance + treasure_chance)
        return [enemy_chance, treasure_chance, empty_chance]

    def get_tiles(self):
        return {d: self.generate_tile for d in self.DIRECTIONS}


map_instance = MapGenerator()

game_map = map_instance.get_tiles()
list_map = [f"{k}:\n"
            f"{v[0]}% enemy\n"
            f"{v[1]}% treasure\n"
            f"{v[2]}% empty" for k, v in game_map.items()]
printable_map = [["",          list_map[0],      ""],
                 [list_map[1], "\nYou are here", list_map[2]],
                 ["",          list_map[3],      ""]]


def current_map():
    p = PrettyTable()
    p.set_style(DOUBLE_BORDER)

    for row in printable_map:
        p.add_row(row)

    return p.get_string(header=False, hrules=True)


def calc_chance_on_map(direction):
    x = randint(1, 100)
    if x <= direction[0]:
        return "You met the enemy"
    elif x <= direction[0] + direction[1]:
        return "You found the treasure"
    else:
        return "You found nothing"


if __name__ == "__main__":
    current_map()
    calc_chance_on_map(direction)
