from random import randint


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


game_map = MapGenerator()
tiles = game_map.get_tiles()
