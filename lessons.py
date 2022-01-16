def is_cat_here(*args):
    if "cat" in args:
        return True
    return False


def is_item_here(item, *args):
    if item in args:
        return True
    return False


def your_favorite_color(my_color, **kwargs):
    if "color" in kwargs:
        print(f"My favorite color is {my_color}, but {kwargs['color']} is also pretty good!")
    else:
        print(f"My favorite color is {my_color}, what is your favorite color?")


# your_favorite_color('red', color="blue", weight=25)
# your_favorite_color('white', shape="round")
