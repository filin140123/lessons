class Rainbow:
    color_number_list = [1, 2, 3, 4, 5, 6, 7]

    def __init__(self):
        pass

    def get_rainbow_color(self, color_number: int):
        if color_number not in self.color_number_list:
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

    def print_neighbour_colors(self, color_number: int):
        center = self.get_rainbow_color(color_number)

        if color_number == self.color_number_list[0]:
            left = self.get_rainbow_color(self.color_number_list[-1])
        else:
            left = self.get_rainbow_color(color_number - 1)

        if color_number == self.color_number_list[-1]:
            right = self.get_rainbow_color(self.color_number_list[0])
        else:
            right = self.get_rainbow_color(color_number + 1)

        print(f"{left} - {center.upper()} - {right}")

    def print_rainbow(self):
        for i in range(self.color_number_list[0], self.color_number_list[-1] + 1):
            print(f"{i}. {self.get_rainbow_color(i)}")


r = Rainbow()
print(r.color_number_list)
print(r.get_rainbow_color(5))
r.print_neighbour_colors(5)
r.print_neighbour_colors(7)
r.print_neighbour_colors(1)
r.print_rainbow()
