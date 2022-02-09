from random import randint


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


current_map = MapGenerator()

game_map = current_map.get_tiles()

list_map = [f"{k}:\n{v[0]}% enemy\n{v[1]}% treasure\n{v[2]}% empty" for k, v in game_map.items()]
printable_map = [["", list_map[0], ""], [list_map[1], "You are here", list_map[2]]]
