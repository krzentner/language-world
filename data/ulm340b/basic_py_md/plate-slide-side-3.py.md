

The robot starts out on the left side of the plate.
The robot should push the plate until it is close enough to the goal location.
''',
        command='button-press-topdown(robot1)',
        button_press_topdown='If the robot\'s gripper is not vertically aligned with the button, put the gripper above the button.',
        drawer_open='If the robot\'s gripper is not vertically aligned with the drawer handle, put the gripper above the drawer handle.',
        door_open='If the robot\'s gripper is not almost vertically aligned with the door handle, put the gripper above the door handle.',
        drawer_close='If the robot\'s gripper is not near the drawer handle, grab the drawer handle.',
        peg_insert_side='If the robot\'s gripper is not vertically aligned with the peg, put the gripper above the peg.',
        window_close='If the window handle is right of the robot\'s gripper and the robot\'s gripper is not near the window handle, move the gripper to the left of the window handle.',
        window_open='If the robot\'s gripper is not vertically aligned with the window handle and the robot\'s gripper is below the window handle, move the gripper to the right of the window handle.',
        pick_place='If the robot\'s gripper is not above the puck, place the gripper above the puck.',
        reach='If the robot\'s gripper is not near the reach target, reach to the goal.',
        push='If the robot\'s gripper is not above the puck and the robot\'s gripper is not vertically aligned with the puck, put the gripper above the puck.'
    ),
    'plate-slide-side':
    TaskInfo(
        name="plate-slide-side",
        intro='Now you have control of a robot with a gripper. The robot can grab objects, but you can also perform more complicated actions by typing instructions into the command line. The goal of this task is to slide a plate to the right. Type instructions, then click "Run", until the plate is in the target location (the red box). Note that you can see the full description of the available instructions by typing "print_help()".',
        command='plate_slide_side(robot1)',
        check='The plate is not in the target location.',
        print_help='Please begin by writing "print_help()" to see available commands.',
        button_press_topdown='If the robot\'s grip