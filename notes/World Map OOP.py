class Room(object):
    def __init__(self, name, north, south, east, west, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.character = []


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
parking_lot = Room("Parking Lot", None, R19A, None)


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


entrance = Room('Entrance', 'carousel', None, None, None, "You're right outside of the amusement "
                       "park. Everything's dark and abandoned.")
carousel = Room('Carousel', None, 'entrance', 'restrooms', 'maze', "The rides should be out of order. You can see the "
                                                        "restrooms to the east. There's a bush maze opposite of it.")
restrooms = Room('Restrooms', None, None, None, 'carousel', "There's a row of stalls in each "
                                                            "restroom. Nothing works anymore.")
maze = Room('Bush Maze', 'adventure_land', 'dead_end', 'carousel', None, "There's only one exit in the maze. "
                       "You feel a murderous presence towards the south.")
dead_end = Room('DEAD END', 'maze', None, None, None, "You find clowns waiting at the end."
                                 " You should turn back around.")
adventure_land = Room('Adventure Land', 'bumper_cars', 'maze', 'rocket_coaster', None, "This is where most of "
                                                                                       "the rides were. "
                                                            "There's a ride straight ahead and another to the right.",)
bumper_cars = Room('Bumper cars', None, adventure_land, None, None, "There's someone riding one of the bumper cars. "
                       "The rides shouldn't be working anymore.")
rocket_coaster = Room('Rocket roller coaster,', None, None, 'train_station', 'adventure_land', "Half of the roller "
                                                                                               "coaster is hanging "
                                                                                               "off of the rails."
                                                                                    " Many accidents happened here.")
train_station = Room('Train Station', 'split_path', None, None, 'rocket_coaster', "You can still ride the train "
                                                                                  "north form here.")
split_path = Room('Split path', None, 'train_station', 'hole', 'tiny_town', "You can go east or west from here. "
                                                                          "You can hear music coming from the west.")
hole = Room('Broken Path', None, None, None, 'split_path', "The rails are broken here and they lead to a "
                       "hole. Anymore and you would've fallen in")
tiny_town = Room('Tiny Town', 'fountain', None, 'split_path', None, "This place is all machine, "
                                                                    "including the people.")
fountain = Room('Fountain', 'food_area', 'tiny_town', 'park', None, "No water flowed from this fountain anymore. "
                       "Looks like it was the center of the town")
park = Room('Tiny Park', None, None, None, 'fountain', "Nothing in the park is green and "
                       "most of the benches were broken.")
food_area = Room('Food Alley', None, 'fountain', None, 'haunted_house', "All the food used to be sold here. "
                       "You can hear a child crying from the west.")
haunted_house = Room('Haunted Mansion', None, None, 'food_area', None, "This is the farthest you can get in the park. "
                       "The child's cries are coming from here.")

