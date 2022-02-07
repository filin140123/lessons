# raise ValueError("Invalid value, retrying...")


def get_rainbow_color(color_number: int):
    color_number_list = [1, 2, 3, 4, 5, 6, 7]
    if color_number not in color_number_list:
        raise ValueError("Invalid color number. Must be integer in range from 1 to 7.")

    if color_number == 1:
        return 'red'
    elif color_number == 2:
        return 'orange'
    elif color_number == 3:
        return 'yellow'
    elif color_number == 4:
        return 'green'
    elif color_number == 5:
        return 'cyan'
    elif color_number == 6:
        return 'blue'
    elif color_number == 7:
        return 'violet'


print(get_rainbow_color(4))
for i in range(1, 8):
    print(get_rainbow_color(i))
# print(get_rainbow_color(9))
# print(get_rainbow_color("4"))
