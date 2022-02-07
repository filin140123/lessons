from ursina import *

app = Ursina()
cube1 = Entity(model="plane", color=color.blue, texture="white_cube", scale=2)
# cube2 = Entity(model="cube", color=color.red, texture="white_cube", scale=2)


def update():
    cube1.rotation_x = cube1.rotation_x + .25
    cube1.rotation_y = cube1.rotation_y + .5
    # cube2.rotation_x = cube2.rotation_x + .25
    # cube2.rotation_y = cube2.rotation_y + .55


app.run()
