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
        super(Knife, self).__init__("Pocket Knife", 10, 10)


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


class Claw(Weapon):
    def __init__(self):
        super(Claw, self).__init__("Claws", 20, 30)


class SledgeHammer(Weapon):
    def __init__(self):
        super(SledgeHammer, self).__init__("Sledge Hammer", 40, 50)


class Armor(Item):
    def __init__(self, name, protection):
        super(Armor, self).__init__(name)
        self.protection = protection
        self.equip = False


class Vest1(Armor):
    def __init__(self):
        super(Vest1, self).__init__("level 1 Armor Vest", 5)


class Vest2(Armor):
    def __init__(self):
        super(Vest2, self).__init__("level 2 Armor Vest", 15)


class Vest3(Armor):
    def __init__(self):
        super(Vest3, self).__init__("level 3 Armor Vest", 30)


class Gloves1(Armor):
    def __init__(self):
        super(Gloves1, self).__init__("Level 1 Gloves", 2)


class Gloves2(Armor):
    def __init__(self):
        super(Gloves2, self).__init__("Level 2 Gloves", 5)


class Gloves3(Armor):
    def __init__(self):
        super(Gloves3, self).__init__("Level 3 Gloves", 10)


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


class Room(object):
    def __init__(self, name, north, south, east, west, description, item, character):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.item = item
        self.character = character


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []

    def move(self, new_location):
        """This moves the player to a new room

        :param new_location: The room object of which you are going to
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """This method searches the current room to see if a room
        exists in that direction.

        :param direction: The direction that you want to move
        :return:
        """
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]


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
            if self.health <= 0:
                print("%s has died" % self.name)
                self.health = 0
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon. damage))
        target.take_damage(self.weapon.damage)

    def death(self):
        if self.health >= 0:
            Room.character = None
            print("They have died.")


entrance = Room('Entrance', 'carousel', None, None, None, "You're right outside of the amusement "
                                                          "park. Everything's dark and abandoned.", Apple(), None)
carousel = Room('Carousel', None, 'entrance', 'restrooms', 'maze', "The rides should be out of order. You can see the "
                                                                   "restrooms to the east. There's a bush maze "
                                                                   "opposite of it.", Knife(), None)
restrooms = Room('Restrooms', None, None, None, 'carousel', "There's a row of stalls in each "
                                                            "restroom. Nothing works anymore.", Gloves1(), None)
maze = Room('Bush Maze', 'adventure_land', 'dead_end', 'carousel', None, "There's only one exit in the maze. "
                                                                         "You feel a murderous presence "
                                                                         "towards the south.", Pistol(), None)
dead_end = Room('DEAD END', 'maze', None, None, None, "You find clowns waiting at the end."
                                                      "You should turn back around.", Bread(), None)
adventure_land = Room('Adventure Land', 'bumper_cars', 'maze', 'rocket_coaster', None, "This is where most of "
                                                                                       "the rides were. "
                                                                                       "There's a ride straight ahead "
                                                                                       "and another to the right.",
                      Vest1(), None)
bumper_cars = Room('Bumper cars', None, 'adventure_land', None, None, "There's someone riding one of the bumper cars. "
                                                                      "The rides shouldn't be working anymore.",
                   Gloves2(), None)
rocket_coaster = Room('Rocket roller coaster,', None, None, 'train_station', 'adventure_land', "Half of the roller "
                                                                                               "coaster is hanging "
                                                                                               "off of the rails."
                                                                                               "Many accidents "
                                                                                               "happened here.",
                      Revolver(), None)
train_station = Room('Train Station', 'split_path', None, None, 'rocket_coaster', "You can still ride the train "
                                                                                  "north form here.", Vest2(), None)
split_path = Room('Split path', None, 'train_station', 'hole', 'tiny_town', "You can go east or west from here. "
                                                                            "You can hear music coming from the west.",
                  Bread(), None)
hole = Room('Broken Path', None, None, None, 'split_path', "The rails are broken here and they lead to a "
                                                           "hole. Anymore and you would've fallen in", Hamburger(),
            None)
tiny_town = Room('Tiny Town', 'fountain', None, 'split_path', None, "This place is all machine, "
                                                                    "including the people.", Machete(), None)
fountain = Room('Fountain', 'food_area', 'tiny_town', 'park', None, "No water flowed from this fountain anymore. "
                                                                    "Looks like it was the center of the town",
                Vest3(), None)
park = Room('Tiny Park', None, None, None, 'fountain', "Nothing in the park is green and "
                                                       "most of the benches were broken.", Gloves3(), None)
food_area = Room('Food Alley', None, 'fountain', None, 'haunted_house', "All the food used to be sold here. "
                                                                        "You can hear a child crying from the west.",
                 Tape(), None)
haunted_house = Room('Haunted Mansion', None, None, 'food_area', None, "This is the farthest you can get in the park. "
                                                                       "The child's cries are coming from here.",
                     Hamburger(), None)


# Weapons
knife = Weapon("Pocket Knife", 15, 10)
pistol = Weapon("Pistol", 5, 50)
machete = Weapon("Machete", 25, 20)
revolver = Weapon("Revolver", 50, 5)
claw = Weapon("Claw", 20, 30)

# Armor
vest1 = Armor("Level 1 Armor Vest", 5)
vest2 = Armor("Level 2 Armor Vest", 15)
vest3 = Armor("Level 3 Armor Vest", 30)
gloves1 = Armor("Level 1 Gloves", 2)
gloves2 = Armor("Level 2 Gloves", 5)
gloves3 = Armor("Level 3 Gloves", 10)

# Consumables
apple = Consumable("Apple", 5)
bread = Consumable("Bread", 10)
milkshake = Consumable("Milkshake", 50)
hamburger = Consumable("Hamburger", 100)
tape = Consumable("Tape", 0)

# Characters
Clown1 = Character("Killer Clown", 50, knife, None)
Clown2 = Character("Killer Clown", 50, knife, None)
Clown3 = Character("Killer Clown", 50, knife, None)
Hound1 = Character("Hell Hound", 10, claw, None)
Hound2 = Character("Hell Hound", 10, claw, None)
Hound3 = Character("Hell Hound", 10, claw, None)
Shadow_Figure1 = Character("Shadow Figure", 100, claw, Vest2)
Shadow_Figure2 = Character("Shadow Figure", 100, claw, Vest2)
Jester = Character("Jester", 300, SledgeHammer, Vest3)

# Player
player = Player(entrance)


playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    print("There's a %s in the area." % player.current_location.item.name)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way")
    elif command.lower() in ['grab']:
        player.inventory.append(player.current_location.item)
        Room.item = None
        print("You have picked up the item.")
    elif command.lower() in ['i, inventory']:
        print(list(player.inventory))
    else:
        print("Command Not Found")



"""
1. Put Items in room  (◉ω◉)
2. Show item is in the room  (◉ω◉)
3. Pick up the item  (◉ω◉)
4. Use the item
"""
