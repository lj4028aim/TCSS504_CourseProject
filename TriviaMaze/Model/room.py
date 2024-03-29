from enum import Enum


class Door(Enum):
    """
    Class 'Door' is a child class of Enum class. It is used to list value for Doors,
    prevent any other values set to door.
    """
    EXIST = "EXIST"
    OPEN = "OPEN"
    CLOSE = "CLOSE"


class Room:
    """
    Class used to represent rooms in the trivia maze game.
    """

    def __init__(self, row, col):
        """
        Initialize new room object with following attributes:
        :param row: an integer number used to represent index of row of the room.
        :param col: an integer number used to represent index of column of the room.
        """
        # flag to indicate the room is exit or not. It is 'False' by default.
        self.__exit = False
        self.row = row
        self.col = col
        # the state of north door.
        self.north = Door.EXIST.value
        # the state of south door.
        self.south = Door.EXIST.value
        # the state of west door.
        self.west = Door.EXIST.value
        # the state of east door.
        self.east = Door.EXIST.value

    def __repr__(self):
        """String representation of Room"""
        return f"r: {self.row} c: {self.col} n: {self.north} s: {self.south} w: {self.west} e: {self.east}"

    def __str__(self):
        """String representation of Room"""
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
