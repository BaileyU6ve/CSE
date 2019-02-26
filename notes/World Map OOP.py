class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west


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


# Option 1 - Define as we go
R19A = Room("Mr. Wiebe's Room")
parking_lot = Room("Parking Lot", None, R19A)

R19A.north = parking_lot

# Option 2 - Set all at once, modify controller
R19A = Room("Mr. Wiebe's Room", 'parking_lot')
parking_lot = Room("Parking Lot", None, R19A)


player = Player(R19A)

playing = True
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way")
    else:
        print("Command Not Found")


entrance = Room('Entrance', 'carousel', None, None, None)
carousel = Room('Carousel', None, 'entrance', 'restrooms', 'maze')
restrooms = Room('Restrooms', None, None, None, 'carousel')
maze = Room('Bush Maze', 'adventure_land', 'dead_end', 'carousel', None)
dead_end = Room('DEAD END', 'maze', None, None, None)
adventure_land = Room('Adventure Land', 'bumper_cars', 'maze', 'rocket_coaster', None)
bumper_cars = Room('Bumper cars', None, adventure_land, None, None)
rocket_coaster = Room('Rocket roller coaster,', None, None, 'train_station', 'adventure_land')
train_station = Room('Train Station', 'split_path', None, None, 'rocket_coaster')
split_path = Room('Split path', None, 'train_station', 'hole', 'tiny_town')
hole = Room('Broken Path', None, None, None, 'split_path')
tiny_town = Room('Tiny Town', 'fountain', None, 'split_path', None)
fountain = Room('Fountain', 'food_area', 'tiny_town', 'park', None)
park = Room('Tiny Park', None, None, None, 'fountain')
food_area = Room('Food Alley', None, 'fountain', None, 'haunted_house')
haunted_house = Room('Haunted Mansion', None, None, 'food_area', None)
