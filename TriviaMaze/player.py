from maze import Maze


class Player:

    def __init__(self, maze, name="monster", golden_key=0):
        self.name = name
        self.maze = maze
        self.coordinates = [1, 1]
        self.golden_key = golden_key
        self.is_golden_key = False

    def move_player(self, x, y):
        updated_x = self.coordinates[0] + x
        updated_y = self.coordinates[1] + y
        if 0 <= updated_x < self.maze.rows and 0 <= updated_y < self.maze.cols:
            self.coordinates[0] = updated_x
            self.coordinates[1] = updated_y

    def reset_player_coordinates(self):
        maze = Maze()
        return self.__init__(maze)

    def get_name(self):
        pass

    def set_name(self):
        pass

    def get_golden_key(self):
        pass

    def set_golden_key(self):
        pass

    def get_is_golden_key(self):
        pass

    def set_is_golden_key(self):
        pass
