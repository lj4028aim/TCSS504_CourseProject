import random


class Adventurer:
    """
    class Adventurer is used to interact with class Dungeon.
    """

    def __init__(self, name, healing_potions=1, vision_potions=1):
        self._name = name
        self.hit_point = random.randrange(75, 100)
        self._number_healing_potions = healing_potions
        self._number_vision_potions = vision_potions
        self.pillar_A = False
        self.pillar_E = False
        self.pillar_I = False
        self.pillar_P = False

    def get_name(self):
        """
        Method is used to get a name when passed in.
        :return: name passed in.
        """
        return str(self._name)

    def set_number_healing_potions(self, cnt):
        self._number_healing_potions = cnt

    def reset_all_pillar(self):
        self.pillar_A = False
        self.pillar_E = False
        self.pillar_I = False
        self.pillar_P = False

    def set_number_vision_potions(self, cnt):
        self._number_vision_potions = cnt

    def set_hit_point(self):
        self.hit_point = random.randrange(75, 100)

    def add_healing_potion(self):
        """
        Method is used to add healing potion if user hit healing potion.
        :return: healing potions
        """
        self._number_healing_potions += 1

    def use_healing_potion(self):
        """
        Method is used track if user uses healing potion.
        :return: updated healing potions.
        """
        if self._number_healing_potions > 0:
            self._number_healing_potions -= 1
            self.hit_point += random.randint(5, 15)

    def add_vision_potion(self):
        """
        Method is used to add vision potions.
        :return: vision potions.
        """
        self._number_vision_potions += 1

    def get_vision_potion(self):
        return self._number_vision_potions

    def get_healing_potion(self):
        return self._number_healing_potions

    def use_vision_potion(self):
        """
        Method is used to track if user uses vision potion.
        :return: updated vision potions.
        """
        if self._number_vision_potions > 0:
            self._number_vision_potions -= 1

    def damage_by_pit(self):
        damage = random.randint(1, 20)
        self.hit_point = max(0, self.hit_point - damage)

    def __str__(self):
        """This method overrides the version from the object class and is called when you print a Adventurer"""
        res = "Name: " + str(self._name) + "\n" \
              + "Hit point: " + str(self.hit_point) + "\n" \
              + "Total Healing Potion: " + str(self._number_healing_potions) + "\n" \
              + "Total Vision Potion: " + str(self._number_vision_potions) + "\n" \
              + "List of Pillars Pieces Found: "
        if self.pillar_A:
            res = res + "Abstraction "
        if self.pillar_E:
            res = res + "Encapsulation "
        if self.pillar_I:
            res = res + "Inheritance "
        if self.pillar_P:
            res = res + "Polymorphism "
        res = res + "\n\n"
        return res
