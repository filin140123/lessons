from importlib import reload

import map_class


while True:
    cmap = map_class.current_map()
    gmap = map_class.game_map
    print(cmap)
    action = input("Where do you want to go?: ")
    for i in map_class.map_instance.DIRECTIONS:
        if action == i:
            print(map_class.calc_chance_on_map(gmap[i]))
    if action in ["quit", "exit", ""]:
        break
    map_class = reload(map_class)
