from enum import Enum


# Enum class to list value for Doors, prevent any other values set to door
class Door(Enum):
    EXIST = "EXIST"
    OPEN = "OPEN"
    CLOSE = "CLOSE"


class Room:
    """
    room class is built to contain a default constructor and the following methods.
    """

    def __init__(self, row, col):
        self.__exit = False
        self.row = row
        self.col = col
        self.north = Door.EXIST.value
        self.south = Door.EXIST.value
        self.west = Door.EXIST.value
        self.east = Door.EXIST.value

    def __repr__(self):
        return f"r: {self.row} c: {self.col} n: {self.north} s: {self.south} w: {self.west} e: {self.east}"

    def __str__(self):
        return f"row: {self.row} column: {self.col} north: {self.north} south: {self.south} west: {self.west} east: " \
               f"{self.east} "

    def update_door_state(self, direction, doorstate):
        """Update doors' state."""
        if direction == "Left":
            self.west = doorstate
        elif direction == "Right":
            self.east = doorstate
        elif direction == "Up":
            self.north = doorstate
        elif direction == "Down":
            self.south = doorstate

    def reset_room(self):
        """Reset the room."""
        self.__exit = False
        self._visited = False
        self.north = Door.EXIST.value
        self.south = Door.EXIST.value
        self.west = Door.EXIST.value
        self.east = Door.EXIST.value

    def get_exit(self):
        """
        Method is used to get the exit.
        :return: self._exit. By default, it returns False.
        """
        return self.__exit

    def set_exit(self, flag):
        """
        Method is used to set the exit depending on flag is True or False.
        :param flag: boolean value, could be True or False.
        :return: True or False
        """
        self.__exit = flag

    def is_exit(self):
        """
        Method is used to test room is an exit or not.
        :return: True or False. By default, it returns False.
        """
        return self.__exit
