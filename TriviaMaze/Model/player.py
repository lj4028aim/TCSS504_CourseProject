class Player:

    def __init__(self, maze, name="monster", golden_key=1):
        self.name = name
        self.maze = maze
        self.coordinates = [1, 1]
        self.golden_key = golden_key
        self.is_golden_key = True

    def move_player(self, x, y):
        updated_x = self.coordinates[0] + x
        updated_y = self.coordinates[1] + y
        if 0 <= updated_x < self.maze._rows and 0 <= updated_y < self.maze._cols:
            self.coordinates[0] = updated_x
            self.coordinates[1] = updated_y

    def reset_player(self):
        self.coordinates = [1, 1]
        self.golden_key = 1
        self.is_golden_key = True

    def get_name(self):
        pass


    def get_golden_key(self):
        """
        Returns the number of golden keys available
        :return: number of golden keys
        """
        return self.golden_key

    def set_golden_key(self):
        pass

    def get_is_golden_key(self):
        pass

    def set_is_golden_key(self):
        pass

    def has_golden_key(self):
        return self.is_golden_key

    def reduce_golden_key(self):
        """
        Reduces the amount of golden keys by 1
        """
        self.golden_key = max(self.golden_key-1, 0)
        if self.golden_key > 0:
            self.set_is_golden_key(True)
        else:
            self.set_is_golden_key(False)
