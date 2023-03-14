class Player:

    def __init__(self, maze, name="monster", golden_key=1):
        self.name = str(name)
        self.maze = maze
        self.coordinates = [1, 1]
        self.golden_key = int(golden_key)
        self.is_golden_key = False

    def move_player(self, x, y):
        updated_x = self.coordinates[0] + x
        updated_y = self.coordinates[1] + y
        if 0 <= updated_x < self.maze._rows and 0 <= updated_y < self.maze._cols:
            self.coordinates[0] = updated_x
            self.coordinates[1] = updated_y

    def reset_player(self):
        self.coordinates = [1, 1]
        self.golden_key = 1
        self.is_golden_key = False

    def get_name(self):
        pass


    def get_golden_key(self):
        """
        Returns the number of golden keys
        :return: number of golden keys
        """
        return self.golden_key

    def set_golden_key(self):
        pass

    def get_is_golden_key(self):
        """Returns True when there is permission to use golden key otherwise False"""
        return self.is_golden_key

    def set_is_golden_key(self, is_golden_key):
        """
        Given True, allows for permission to use golden key
        :param is_golden_key: boolean, permission to use golden key
        """
        self.is_golden_key = is_golden_key

    def has_golden_key(self):
        """Checks if there is a golden key is available"""
        return self.golden_key > 0

    def reduce_golden_key(self):
        """Reduces the amount of golden keys by 1"""
        self.golden_key = max(self.golden_key-1, 0)
