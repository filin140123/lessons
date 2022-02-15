class Coordinates:
    __START_POINT = [0, 0]
    stored_positions = []
    visited_positions = []
    current_pos = __START_POINT

    def __str__(self):
        return str(self.current_pos)

    def write_coordinates(self):
        self.stored_positions.append(self.current_pos[:])
        if self.current_pos not in self.visited_positions:
            self.visited_positions.append(self.current_pos[:])

    def moving_on_coordinates(self, direction):
        if direction == "up":
            self.current_pos[1] += 1
        elif direction == "left":
            self.current_pos[0] -= 1
        elif direction == "right":
            self.current_pos[0] += 1
        elif direction == "down":
            self.current_pos[1] -= 1

    def check_coordinates_around(self):
        up = [self.current_pos[0], self.current_pos[1] + 1]
        left = [self.current_pos[0] - 1, self.current_pos[1]]
        right = [self.current_pos[0] + 1, self.current_pos[1]]
        down = [self.current_pos[0], self.current_pos[1] - 1]
        dir_dict = {'up': up, 'left': left, 'right': right, 'down': down}
        return {k: 'Already\nvisited...' for k, v in dir_dict.items() if v in self.visited_positions}

    def get_distance(self):
        return len(self.stored_positions)

    def get_visited_positions(self):
        return len(self.visited_positions)


coor = Coordinates()
