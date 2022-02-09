from random import randint
from importlib import reload

import map_class
from prettytable import PrettyTable, DOUBLE_BORDER


def current_map():
    p = PrettyTable()
    p.set_style(DOUBLE_BORDER)

    pmap = map_class.printable_map
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


while True:
    cmap = current_map()
    gmap = map_class.game_map
    print(cmap)
    print(gmap)
    action = input("Where do you want to go?: ")
    if action == "up":
        print(calc_chance_on_map(gmap["up"]))
    elif action == "left":
        print(calc_chance_on_map(gmap["left"]))
    elif action == "right":
        print(calc_chance_on_map(gmap["right"]))
    elif action in ["quit", "exit", ""]:
        break
    map_class = reload(map_class)
