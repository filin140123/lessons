from importlib import reload

import map_class


while True:
    cmap = map_class.current_map()
    gmap = map_class.game_map
    print(cmap)
    print(gmap)
    action = input("Where do you want to go?: ")
    if action == "up":
        print(map_class.calc_chance_on_map(gmap["up"]))
    elif action == "left":
        print(map_class.calc_chance_on_map(gmap["left"]))
    elif action == "right":
        print(map_class.calc_chance_on_map(gmap["right"]))
    elif action in ["quit", "exit", ""]:
        break
    map_class = reload(map_class)
