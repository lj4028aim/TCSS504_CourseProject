class Room:
    """
    class Room is built to contain a default constructor and the following methods.
    """

    def __init__(self, row, col):
        self.__healthPotion = False
        self.__visionPotion = False
        self.__hasPillar = False
        self._healthPotion = False
        self._visionPotion = False
        self._pillar = "No pillar"
        self._pit = False
        self._exit = False
        self._entrance = False
        self._visited = False
        self.__impassable = False
        self.row = row
        self.col = col
        self.north = False
        self.south = False
        self.west = False
        self.east = False

    def __str__(self):
        """
        Method is used to build a 2D Graphical representation of the room.
        :return: shape of room
        """
        res = ""
        res += "* - *\n" if self.north else "*****\n"
        res += "|" if self.west else "*"
        if self._healthPotion and self._visionPotion:
            res += " M "
        elif self._healthPotion:
            res += " H "
        elif self._visionPotion:
            res += " V "
        elif self._pit:
            res += " X "
        elif self._exit:
            res += " O "
        elif self._entrance:
            res += " i "
        elif self._pillar == "Abstraction":
            res += " A "
        elif self._pillar == "Encapsulation":
            res += " E "
        elif self._pillar == "Inheritance":
            res += " I "
        elif self._pillar == "Polymorphism":
            res += " P "
        else:
            res += "   "
        res += "|\n" if self.east else "*\n"
        res += "* - *\n" if self.south else "*****\n"
        return res

    def get_health_potion(self):
        """
        Method is used to get health potion.
        :return: healthPotion. By default, it returns False.
        """
        return self._healthPotion

    def set_health_potion(self, bool):
        """
        Method is used to set health potion depending on boolean value passed in.
        :param bool: boolean value. It could be True or False.
        :return: True or False
        """
        self._healthPotion = bool

    def get_vision_potion(self):
        """
        Method is used to get vision potion.
        :return: visionPotion  By default, it returns False.
        """
        return self._visionPotion

    def set_vision_potion(self, bool):
        """
        Method is used to set vision potion depending on boolean value passed in.
        :param bool: boolean value. It could be True or False.
        :return: True or False.
        """
        self._visionPotion = bool

    def get_pillar(self):
        """
        Method is used to get pillar.
        :return: self._pillar. By default, it returns "No Pillar".
        """
        return self._pillar

    def set_pillar(self, pillar):
        """
        Method is used to set pillars.
        :param pillar: one element of a list ["Abstraction", "Encapsulation", "Inheritance", "Polymorphism"].
        :return: whichever pillar passed in.
        """
        self._pillar = pillar

    def get_pit(self):
        """
        Method is used to get pit.
        :return: self._pit. By default, it returns False.
        """
        return self._pit

    def set_pit(self, bool):
        """
        Method is used to set pit depending on boolean value passed in.
        :param bool: It is a boolean value; could be True or False.
        :return: True or False.
        """
        self._pit = bool

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

    def set_pillar(self, pillar):
        self._pillar = pillar

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

    def set_health(self, add_potion):
        """
        Method is used to set health.
        :param add_potion:
        :return:
        """
        self._healthPotion = add_potion

    def set_vision(self, add_vision):
        """
        Method is used to set the vision.
        :param add_vision:
        :return:
        """
        self.__visionPotion = add_vision

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

    def get_has_pit(self):
        """
        Method is used to get get_pit method.
        :return:
        """
        return self._pit
