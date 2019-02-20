class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None):
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


entrance = Room('Entrance', 'carousel')
carousel = Room('Carousel', None, 'entrance', 'restrooms', 'maze')
restrooms = Room('Restrooms', None, None, None, 'carousel')
maze = Room('Bush Maze', 'adventure_land', 'dead_end', 'carousel')
dead_end = Room('DEAD END', 'maze')
adventure_land= Room('Adventure Land', 'bumper_cars', 'maze', 'rocket_coaster')


