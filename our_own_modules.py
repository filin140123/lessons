# utils.py
def get_favorite_color():
    return "super-duper color"


def get_favorite_number():
    return 13


# main_file.py
import utils

color = utils.get_favorite_color()
number = utils.get_favorite_number()

print(color, number)
