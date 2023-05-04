
- Steps: 1. Put the gripper above the handle  2. Push down the handle
'''

def get_task_info(task_name, info_index, print_info = True, print_options = True):
    task_name = ' '.join(task_name.split('_'))
    task_to_instructions = {
        'reach': {'options': [('robot\'s gripper', 'reach towards the target'),
                             ('robot\'s gripper', 'not near reach target')]},

        'push': {'options': [('robot\'s gripper', 'push gripper into top of puck'),
                         ('robot\'s gripper', 'not above puck'),
                         ('robot\'s gripper', 'put gripper above the puck'),
                         ('robot\'s gripper', 'not near puck'),
                         ('robot\'s gripper', 'not vertically aligned with puck')]},

        'door-open': {'options': [('robot\'s gripper', 'put gripper above door handle'),
                             ('robot\'s gripper', 'not almost vertically aligned with door handle'),
                             ('robot\'s gripper', 'put gripper around door handle'),
                             ('robot\'s gripper', 'open'),
                             ('robot\'s gripper', 'almost vertically aligned with the door handle'),
                             ('robot\'s gripper', 'pull open the door'),
                             ('robot\'s gripper', 'vertically aligned with the door handle')]},

        'drawer-open': {'options': [('robot\'s gripper', 'put gripper above drawer handle'),
                             ('robot\'s gripper', 'not vertically aligned with drawer handle'),
                             ('robot\'s gripper', 'not around drawer handle'),
                             ('robot\'s gripper', 'put gripper around drawer handle'),
                             ('robot\'s gripper', 'vertically aligned with drawer handle'),
                             ('robot\'s gripper', 'pull open the drawer'),
                             ('robot\'s gripper', 'around drawer handle')]},

        'window-close': {'options': [('window handle', 'right of the robot\'s gripper'),
                             ('robot\'s gripper', '