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
        'NAME': "The Carousel ride",
        'DESCRIPTION': "The rides should be out of order.",
        'PATHS': {
            'EAST': 'RESTROOMS',
            'WEST': 'MAZE',
            'SOUTH': 'ENTRANCE'
        }
    }
}
