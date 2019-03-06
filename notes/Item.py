class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage, durability):
        super(Weapon, self).__init__(name)
        self.damage = damage
        self.durability = durability

    def use_weapon(self):
        self.durability -= 5
        print("Your weapon's durability gets lower.")


class Knife(Weapon):
    def __init__(self):
        super(Knife, self).__init__("Pocket Knife", 20, 55)


class Pistol(Weapon):
    def __init__(self):
        super(Pistol, self).__init__("Pistol", 5, 100)


class Machete(Weapon):
    def __init__(self):
        super(Machete, self).__init__("Machete", 40, 75)

class Armor(Item):
    def __init__(self, name, protection, durability):
        super(Armor, self).__init__(name)
        self.protection = protection
        





