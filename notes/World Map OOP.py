class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, up=None, down=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
       


# Option 1 - Define as we go
R19A = Room("Mr. Wiebe's Room")
parking_lot = Room("Parking Lot", None, R19A)

R19A.north = parking_lot

# Option 2 - Set all at once, modify controller
R19A = Room("Mr. Wiebe's Room", 'parking_lot')
parking_lot = Room("Parking Lot", None, R19A)


entrance = Room('Entrance', 'carousel', None, None, None)
carousel = Room('Carousel', None, 'entrance', 'restrooms', 'maze')
restrooms = Room('Restrooms', None, None, None, 'carousel')
maze = Room('Bush Maze', 'adventure_land', 'dead_end', 'carousel', None)
dead_end = Room('DEAD END', 'maze')
adventure_land = Room('Adventure Land', 'bumper_cars', 'maze', 'rocket_coaster')
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
