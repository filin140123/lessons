from importlib import reload
from random import randint

from prettytable import PrettyTable, DOUBLE_BORDER

import worldmap
from coordinates import coor
from inventory import player_inventory
from health import player_health

statistics = {
    "treasures": 0,
    "enemies": 0,
}


def current_map(visited_tile):
    temp_dict = worldmap.tiles
    temp_dict.update(visited_tile)
    list_map = []
    for k, v in temp_dict.items():
        if isinstance(v, str):
            list_map.append(f"{k}:\n"
                            f"{v}")
        else:
            list_map.append(f"{k}:\n"
                            f"{v[0]}% enemy\n"
                            f"{v[1]}% treasure\n"
                            f"{v[2]}% empty")

    printable_map = [["\n???", list_map[0], "\n???"],
                     [list_map[1], "\nYou are here", list_map[2]],
                     ["\n???", list_map[3], "\n???"]]

    p = PrettyTable()
    p.set_style(DOUBLE_BORDER)
    for row in printable_map:
        p.add_row(row)

    return p.get_string(header=False, hrules=True)


def calc_chance_on_map(direction, current_position: list, visited_positions: list):
    if current_position in visited_positions:
        return "Already visited"  # TODO: Event placeholder

    x = randint(1, 100)
    if x <= direction[0]:
        statistics["enemies"] += 1
        player_health.health_down(5)  # TODO: Player health down test
        player_inventory.append_item("loot")  # TODO: Reward for killing enemy test
        return "You met the enemy"  # TODO: Event placeholder
    elif x <= direction[0] + direction[1]:
        statistics["treasures"] += 1
        player_inventory.append_item("coin")  # TODO: Item Appending test
        return "You found the treasure"  # TODO: Event placeholder
    else:
        return "You found nothing"  # TODO: Event placeholder


while True:
    cmap = current_map(coor.check_coordinates_around())
    print(cmap)
    # print(worldmap.tiles)
    print("current position:", coor)
    print("tiles traveled:", coor.get_distance(), "|", "unique tiles:", coor.get_visited_positions())
    # print("all:", coor.stored_positions)
    # print("unique:", coor.visited_positions)
    print("Health:", player_health)
    print("Inventory:", player_inventory)
    print(statistics)

    action = input("Where do you want to go?: ")

    for d in worldmap.game_map.DIRECTIONS:
        if action == d:
            coor.write_coordinates()
            coor.moving_on_coordinates(d)
            print(calc_chance_on_map(worldmap.tiles[d], coor.current_pos, coor.visited_positions))
            worldmap = reload(worldmap)

    if action.startswith("discard "):
        tmp_action = action.split(" ")
        tmp_action[1] = "".join(tmp_action[1:])
        player_inventory.discard_item(tmp_action[1])

    if action in ["quit", "exit"]:
        break

    if not player_health.is_alive():
        print("Game Over")
        break
