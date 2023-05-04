
    - 
""")


# noinspection SpellCheckingInspection
def get_step_examples(robot, steps, task):
    return [
        ('reach', 'Reach towards the target',
            ('the robot\'s gripper is not near reach target', 'the robot\'s gripper is near the reach target'),
            ['When the robot\'s gripper is not near reach target, move the robot\'s gripper until the robot\'s gripper is near the reach target']),
        ('push', 'Slide the puck to the target location',
            ('the robot\'s gripper is not above puck and the robot\'s gripper is not vertically aligned with the puck', 'the robot\'s gripper is near the puck and the puck is below the robot\'s gripper'),
            [
                'When the robot\'s gripper is not above puck and the robot\'s gripper is not vertically aligned with the puck, move the robot\'s gripper until the robot\'s gripper is vertically aligned with the puck',
                'When the robot\'s gripper is vertically aligned with the puck and the robot\'s gripper is not near puck, move the robot\'s gripper until the robot\'s gripper is above the puck and the robot\'s gripper is closed',
                'When the robot\'s gripper is near the puck and the puck is below the robot\'s gripper, move the robot\'s gripper until the robot\'s gripper is above the target location'
            ]),
        ('window-close', 'Slide the window closed to the right',
            ('the robot\'s gripper is in front of the window handle', 'the window handle is right of the robot\'s gripper and the robot\'s gripper is not near the window handle'),
            [
                'When the robot\'s gripper is in front of the window handle, move the robot\'s gripper until the robot\'s gripper is right of the window handle',
                'When the window handle is right of the robot\'s gripper and the robot\'s gripper is not near the window handle, move the robot\'s gripper until the robot\'s gripper is almost vertically aligned with the window handle',
                'When the robot\'s gripper is near the window handle, move the robot\'s gripper until the robot\'s gripper is forward aligned with the window handle'
            ]),
        ('button-press-topdown', 'Push the button