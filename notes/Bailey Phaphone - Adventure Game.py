world_map = {
    'ENTRANCE': {
        'NAME': "Entrance",
        'DESCRIPTION': "You're right outside of the amusement "
                       "park. Everything's dark and abandoned.",
        'PATHS': {
            'NORTH': 'CAROUSEL'
        }
    },
    'CAROUSEL': {
        'NAME': "Carousel ride",
        'DESCRIPTION': "The rides should be out of order. You can see the "
                       "restrooms to the east. There's a bush maze opposite of it.",
        'PATHS': {
            'EAST': 'RESTROOMS',
            'WEST': 'MAZE',
            'SOUTH': 'ENTRANCE'
        }
    },
    'RESTROOMS': {
        'NAME': "Restrooms",
        'DESCRIPTION': "There's a row of stalls in each restroom. Nothing works anymore.",
        'PATHS': {
            'WEST': 'CAROUSEL'
        }
    },
    'MAZE': {
        'NAME': "Bush Maze",
        'DESCRIPTION': "There's only one exit in the maze. "
                       "You feel a murderous presence towards the south.",
        'PATHS': {
            'SOUTH': 'DEAD_END',
            'NORTH': 'ADVENTURE_LAND',
            'EAST': 'CAROUSEL'
        }
    },
    'DEAD_END': {
        'NAME': "Dead end",
        'DESCRIPTION': "You find clowns waiting at the end."
                       " You should turn back around.",
        'PATHS': {
            'NORTH': 'MAZE'
        }
    },
    'ADVENTURE_LAND': {
        'NAME': "Adventure Land",
        'DESCRIPTION': "This is where most of the rides were. "
                       "There's a ride straight ahead and another to the right.",
        'PATHS': {
            'NORTH': 'BUMPER_CARS',
            'EAST': 'ROCKET_COASTER',
            'SOUTH': 'MAZE'
        }
    },
    'BUMPER_CARS': {
        'NAME': "Bumper Cars",
        'DESCRIPTION': "There's someone riding one of the bumper cars. "
                       "The rides shouldn't be working anymore.",
        'PATHS': {
            'SOUTH': 'ADVENTURE_LAND'
        }
    },
    'ROCKET_COASTER': {
        'NAME': "Rocket Coaster",
        'DESCRIPTION': "Half of the roller coaster is hanging off of the rails."
                       " Many accidents happened here.",
        'PATHS': {
            'EAST': 'TRAIN_STATION',
            'WEST': 'ADVENTURE_LAND'
        }
    },
    'TRAIN_STATION': {
        'NAME': "Train",
        'DESCRIPTION': "You can still ride the train north form here.",
        'PATHS': {
            'NORTH': 'SPLIT_PATH',
            'WEST': 'ROCKET_COASTER'
        }
    },
    'SPLIT_PATH': {
        'NAME': "Split Path",
        'DESCRIPTION': "You can go east or west from here. "
                       "You can hear music coming from the west.",
        'PATHS': {
            'EAST': 'HOLE',
            'WEST': 'TINY_TOWN',
            'SOUTH': 'TRAIN_STATION'
        }
    },
    'HOLE': {
        'NAME': "Broken Path",
        'DESCRIPTION': "The rails are broken here and they lead to a "
                       "hole. Anymore and you would've fallen in",
        'PATHS': {
            'WEST': 'SPLIT_PATH'
        }
    },
    'TINY_TOWN': {
        'NAME': "Tiny Town",
        'DESCRIPTION': "This place is all machine, including the people.",
        'PATHS': {
            'NORTH': 'FOUNTAIN',
            'EAST': 'SPLIT_PATH'
        }
    },
    'FOUNTAIN': {
        'NAME': "Fountain",
        'DESCRIPTION': "No water flowed from this fountain anymore. "
                       "Looks like it was the center of the town",
        'PATHS': {
            'NORTH': 'FOOD_AREA',
            'EAST': 'PARK',
            'SOUTH': 'TINY_TOWN'
        }
    },
    'PARK': {
        'NAME': "Tiny Park",
        'DESCRIPTION': "Nothing in the park is green and "
                       "most of the benches were broken.",
        'PATHS': {
            'WEST': 'FOUNTAIN'
        }
    },
    'FOOD_AREA': {
        'NAME': "Food Alley",
        'DESCRIPTION': "All the food used to be sold here. "
                       "You can hear a child crying from the west.",
        'PATHS': {
            'WEST': 'HAUNTED_HOUSE',
            'SOUTH': 'FOUNTAIN'
        }
    },
    'HAUNTED_HOUSE': {
        'NAME': "Haunted Mansion",
        'DESCRIPTION': "This is the farthest you can get in the park. "
                       "The child's cries are coming from here.",
        'PATHS': {
            'EAST': 'FOOD_AREA'
        }
    }
}


playing = True
current_node = world_map['ENTRANCE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']
while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way")
    else:
        print("Command Not Found")
