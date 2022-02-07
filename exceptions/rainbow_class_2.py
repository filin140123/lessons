class Rainbow:
    def __init__(self, color_list: list):
        self.color_list = color_list

    def get_color_by_index(self, color_number: int):
        if not self.color_list[color_number - 1]:
            raise ValueError(f"Invalid color number. Must be integer in range from 1 to {len(self.color_list)}.")

        return self.color_list[color_number - 1]

    def get_neighbours_by_index(self, color_number: int, pretty=False):
        center = self.get_color_by_index(color_number)

        if color_number == 1:
            left = self.color_list[-1]
        else:
            left = self.get_color_by_index(color_number - 1)

        if color_number == len(self.color_list):
            right = self.color_list[0]
        else:
            right = self.get_color_by_index(color_number + 1)

        if pretty:
            return f"{left} <- {center.upper()} -> {right}"
        else:
            return left, center, right

    def print_all_colors(self):
        for i in range(1, len(self.color_list) + 1):
            print(f"{i}. {self.get_color_by_index(i)}")


rainbow_colors = ["red", "orange", "yellow", "green", "cyan", "blue", "violet"]

r = Rainbow(rainbow_colors)
print(r.color_list)
print(r.get_color_by_index(5))
print(r.get_neighbours_by_index(5))
print(r.get_neighbours_by_index(7))
print(r.get_neighbours_by_index(1, pretty=True))
r.print_all_colors()
