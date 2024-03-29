class Player:

    def __init__(self, maze, name="monster", golden_key=5):
        """
        Initialize a new instance of Player

        :param maze: maze used in the game
        :param name: by default, the name is 'monster'
        :param golden_key: be default, the golden_key is set to 10
        """
        self.name = str(name)
        self.maze = maze
        self.coordinates = [1, 1]
        self.golden_key = int(golden_key)
        self.is_golden_key = False

    def __repr__(self):
        """Returns string representation of Player object"""
        return f"name: {self.name}, # of golden keys: {self.golden_key}, is a golden key: {self.is_golden_key}"

    def move_player(self, x, y):
        """
        Moves the position of Player to then given coordinates.

        :param x: horizontal coordinate
        :param y: vertical coordinate
        """
        updated_x = self.coordinates[0] + x
        updated_y = self.coordinates[1] + y
        if 0 <= updated_x < self.maze._rows and 0 <= updated_y < self.maze._cols:
            self.coordinates[0] = updated_x
            self.coordinates[1] = updated_y

    def reset_player(self):
        """Reset player's coordinate."""
        self.coordinates = [1, 1]
        self.golden_key = 5
        self.is_golden_key = False

    def set_golden_key(self, set_golden_key):
        """Set golden key cnt"""
        self.golden_key = int(set_golden_key)
    def get_name(self):
        """
        Returns the player name
        """
        return self.name

    def set_name(self, name):
        """
        Set the player name
        """
        self.name = str(name)

    def get_golden_key(self):
        """
        Returns the number of golden keys

        :return: number of golden keys
        """
        return self.golden_key

    def get_is_golden_key(self):
        """
        Returns True when there is permission to use golden key otherwise False

        :return: boolean, there is permission to use a golden key
        """
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
