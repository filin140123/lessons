import random


def my_function(a, b, func):
    result = func([a, b])
    return result


print(my_function(2, 3, sum))


def colorize(thing):
    def get_color():
        colors = ('red', 'green', 'blue')
        color = random.choice(colors)
        return color

    return f"{get_color()} {thing}"


# testing
for i in range(10):
    print(colorize('apple'), end="\n" if i == 9 else ", ")
