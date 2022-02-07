colors_list = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'violet']
with open("rainbow.txt", "w") as rainbow:
    for color in colors_list:
        print(color, file=rainbow)
