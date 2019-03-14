class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage, durability):
        super(Weapon, self).__init__(name)
        self.damage = damage
        self.durability = durability

    def swing_weapon(self):
        self.durability -= 1
        print("Your weapon's durability gets lower.")
        if self.durability == 0:
            print("Your weapon is out of durability. Tape can be used to fix it")


class Knife(Weapon):
    def __init__(self):
        super(Knife, self).__init__("Pocket Knife", 15, 10)


class Pistol(Weapon):
    def __init__(self):
        super(Pistol, self).__init__("Pistol", 5, 50)

    def shootpistol(self):
        self.durability -= 1
        print("You're ammo is getting lower.")


class Machete(Weapon):
    def __init__(self):
        super(Machete, self).__init__("Machete", 25, 20)


class Revolver(Weapon):
    def __init__(self):
        super(Revolver, self).__init__("Revolver", 50, 5)

    def shootrevolver(self):
        self.durability -= 1
        print("The revolver has limited ammo.")


class Armor(Item):
    def __init__(self, name, protection):
        super(Armor, self).__init__(name)
        self.protection = protection
        self.equip = False


class Vest1(Armor):
    def __init__(self):
        super(Vest1, self).__init__("level 1 Armor Vest ", 5)


class Vest2(Armor):
    def __init__(self):
        super(Vest2, self).__init__("level 2 Armor Vest ", 15)


class Vest3(Armor):
    def __init__(self):
        super(Vest3, self).__init__("level 3 Armor Vest ", 30)


class Gloves1(Armor):
    def __init__(self):
        super(Gloves1, self).__init__("Level 1 Gloves ", 2)


class Gloves2(Armor):
    def __init__(self):
        super(Gloves2).__init__("Level 2 Gloves", 5)


class Gloves3(Armor):
    def __init__(self):
        super(Gloves3).__init__("Level 3 Gloves", 10)


class Consumable(Item):
    def __init__(self, name, recovery):
        super(Consumable, self).__init__(name)
        self.recovery = recovery


class Apple(Consumable):
    def __init__(self):
        super(Apple, self).__init__("Apple", 5)


class Bread(Consumable):
    def __init__(self):
        super(Bread, self).__init__("Bread", 10)


class Milkshake(Consumable):
    def __init__(self):
        super(Milkshake, self).__init__("Milkshake", 50)


class Hamburger(Consumable):
    def __init__(self):
        super(Hamburger, self).__init__("Hamburger", 100)


class Tape(Consumable):
    def __init__(self):
        super(Tape, self).__init__("Tape", 0)


class Character(object):
    def __init__(self, name, health: int, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage: int):
        if self.armor.protection > damage:
            print("No damage is done because of some AMAZING armor.")
        else:
            self.health -= damage - self.armor.protection
            print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon. damage))
        target.take_damage(self.weapon.damage)


# Items
Knife = Weapon("Sword", 15, 10)
Machete = Weapon("Canoe", 25, 20)
Vest3 = Armor("Armor of the gods", 30)

# Characters
orc = Character("Orc1", 100, Knife, Armor("Gloves1", 3))
orc2 = Character("Wiebe", 10000, Machete, Vest3)

orc.attack(orc2)
orc2.attack(orc)
orc2.attack(orc)
orc2.attack(orc)
