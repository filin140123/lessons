from random import randint
from prettytable import PrettyTable, DOUBLE_BORDER


class MapGenerator:
    __TOTAL_CHANCE = 100
    __DIRECTIONS = ["up", "left", "right"]

    @property
    def generate_tile(self):
        enemy_chance = randint(25, 50)
        treasure_chance = randint(5, 15)
        empty_chance = self.__TOTAL_CHANCE - (enemy_chance + treasure_chance)
        return [enemy_chance, treasure_chance, empty_chance]

    def get_tiles(self):
        return {d: self.generate_tile for d in self.__DIRECTIONS}


map_instance = MapGenerator()

game_map = map_instance.get_tiles()
list_map = [f"{k}:\n{v[0]}% enemy\n{v[1]}% treasure\n{v[2]}% empty" for k, v in game_map.items()]
printable_map = [["", list_map[0], ""], [list_map[1], "You are here", list_map[2]]]


def current_map():
    p = PrettyTable()
    p.set_style(DOUBLE_BORDER)

    pmap = printable_map
    for row in pmap:
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
    calc_chance_on_map(direction)
    current_map()
