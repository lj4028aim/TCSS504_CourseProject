class Player:

    def __init__(self, name = "Player", golden_key = 0):
        self.name = str(name)
        self.golden_key = golden_key
        self.is_golden_key = False

    def __repr__(self):
        return f"name: {self.name}, # of golden keys: {self.golden_key}, is a golden key: {self.is_golden_key}"

    def get_name(self):
        """
        Returns the player name
        :return: name of player
        """
        return self.name

    def set_name(self, name):
        """
        Sets the name of the player
        :param name: name of player
        """
        self.name = name

    def get_golden_key(self):
        """
        Returns the number of golden keys available
        :return: number of golden keys
        """
        return self.golden_key

    def set_golden_key(self, golden_key):
        """
        Sets the number of golden keys
        :param golden_key: number of golden keys
        """
        self.golden_key = golden_key

    def get_is_golden_key(self):
        """
        Returns true when there is a golden key
        :return: True if there is a golden key
        """
        return self.is_golden_key == True

    def set_is_golden_key(self, is_golden_key):
        """
        Sets if there is a golden key
        :param is_golden_key: boolean, if there is a golden key
        """
        self.is_golden_key = is_golden_key

if __name__ == "__main__":
    player = Player()
    print(player.__repr__())
    player.set_name("Dev")
    print(player.__repr__())
    print(player.get_golden_key())
    player.set_golden_key(5)
    print(player.__repr__())
    print(player.get_is_golden_key())
    player.set_is_golden_key(True)
    print(player.__repr__())