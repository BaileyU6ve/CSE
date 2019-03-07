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
        super(Pistol, self).__init__("Pistol", 5, 80)

    def shoot(self):
        self.durability -= 1
        print("You're ammo is getting lower.")


class Machete(Weapon):
    def __init__(self):
        super(Machete, self).__init__("Machete", 40, 75)


class Armor(Item):
    def __init__(self, name, protection):
        super(Armor, self).__init__(name)
        self.protection = protection
        self.equip = False

    def equip(self):
        self.equip = True

    def unequip(self):
        self.equip = False


class Vest1(Armor):
    def __init__(self):
        super(Vest1, self).__init__("Armor Vest level 1", 5)


class Vest2(Armor):
    def __init__(self):
        super(Vest2, self).__init__("Armor Vest level 2", 15)


class Vest3(Armor):
    def __init__(self):
        super(Vest3, self).__init__("Armor Vest level 3", 30)


class Consumable(Item):
    def __init__(self, name, recovery):
        super(Consumable, self).__init__(name)
        self.recovery = recovery


class Apple(Consumable):
    def __init__(self):
        super(Apple, self).__init__("Apple", 5)


