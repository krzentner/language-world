
"""


def is_button(state):
    return state['target']['objectType'] == 'Button'

def is_drawer(state):
    return state['target']['objectType'] == 'Drawer'

def is_door(state):
    return state['target']['objectType'] == 'Door'

def is_window(state):
    return state['target']['objectType'] == 'Window'

def is_peg(state):
    return state['target']['objectType'] == 'Peg'

def is_drawer_closed(state):
    drawer_x = state['target']['location']['x']
    drawer_y = state['target']['location']['y']
    drawer_height = state['target']['height']

    if drawer_y + drawer_height >= drawer_x:
        return 0
    else:
        return drawer_y + drawer_height - drawer_x + 1

def is_drawer_open(state):
    drawer_x = state['target']['location']['x']
    drawer_y = state['target']['location']['y']
    drawer_height = state['target']['height']

    if drawer_y + drawer_height <= drawer_x:
        return 0
    else:
        return drawer_x - (drawer_y + drawer_height) + 1

def is_door_closed(state):
    door_x = state['target']['location']['x']
    door_y = state['target']['location']['y']
    door_width = state['target']['width']

    if door_x + door_width >= door_y:
        return 0
    else:
        return door_x + door_width - door_y + 1

def is_door_open(state):
    door_x = state['target']['location']['x']
    door_y = state['target']['location']['y']
    door_width = state['target']['width']

    if door_x + door_width <= door_y:
        return 0
    else:
        return door_y - (door_x + door_width) + 1

def is_window_closed(state):
    window_x = state['target']['location']['x']
    window_y = state['target']['location']['y']
    window_width = state['target']['width']

    if window_y