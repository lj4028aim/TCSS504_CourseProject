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
        self._exit = False
        self._entrance = False
        self._visited = False
        self.row = row
        self.col = col
        self.north = Door.EXIST.value
        self.south = Door.EXIST.value
        self.west = Door.EXIST.value
        self.east = Door.EXIST.value


    def __str__(self):
        """
        Method is used to build a 2D Graphical representation of the room.
        :return: shape of room
        """
        res = ""
        res += "* - *\n" if self.north else "*****\n"
        res += "|" if self.west else "*"
        if self._exit:
            res += " O "
        elif self._entrance:
            res += " i "
        else:
            res += "   "
        res += "|\n" if self.east else "*\n"
        res += "* - *\n" if self.south else "*****\n"
        return res

    def get_exit(self):
        """
        Method is used to get the exit.
        :return: self._exit. By default, it returns False.
        """
        return self._exit

    def set_exit(self, flag):
        """
        Method is used to set the exit depending on flag is True or False.
        :param flag: boolean value, could be True or False.
        :return: True or False
        """
        self._exit = flag

    def get_entrance(self):
        """
        Method is used to get the entrance.
        :return: self._entrance. By default, it returns False.
        """
        return self._entrance

    def set_entrance(self, flag):
        """
        Method is used to set the entrance depending on flag is True or False.
        :param flag: boolean value, could be True or False.
        :return: True or False
        """
        self._entrance = flag

    def __repr__(self):
        """
        :return: calling __str__ method.
        """
        return str(self)

    def draw_top(self):
        """
        Method is used to draw north portion of room.
        :return: shape of north portion of room.
        """
        if self.north:
            print("*   *", end="")
        else:
            print("*****", end="")

    def draw_middle(self):
        """
        Method is used to draw west and/or east portion of room.
        :return: shape of west and/or east portion of room.
        """
        if self.west:
            print(" ", end="")
        else:
            print("*", end="")
        print("   ", end="")
        if self.east:
            print(" ", end="")
        else:
            print("*", end="")

    def draw_bottom(self):
        """
        Method is used to draw south portion of room.
        :return: shape of south portion of room.
        """
        if self.south:
            print("*   *", end="")
        else:
            print("*****", end="")

    def can_enter(self):
        """
        Method is used test if user could enter.
        :return: possible entrance.
        """
        return not self.__impassable and not self._visited

    def is_exit(self):
        """
        Method is used to test room is an exit or not.
        :return: True or False. By default, it returns False.
        """
        return self._exit

    def set_visited(self, visited):
        """
        Method is used to set rooms have been visited to True or False.
        :param visited: boolean value. True or False.
        :return: self._visited. By default, it returns False.
        """
        self._visited = visited
