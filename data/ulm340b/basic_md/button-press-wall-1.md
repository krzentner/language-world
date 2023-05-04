

The task `pick-place-bin` requires the robot to pick up the puck and place it in the bin.
To pick up the puck and place it in the bin reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the puck, the robot should place gripper above puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, the robot should drop gripper around puck.
    - When the robot's gripper is near puck and the robot's gripper is open, the robot should close gripper around puck.
    - When the robot's gripper is above puck and the robot's gripper is closed, the robot should place puck in bin.

The task `button-press-bin` requires the robot to press the button at the bottom of the bin.
To press the button at the bottom of the bin reliably, the robot should perform the following steps:
    - When the robot's gripper is not above button and the robot's gripper is not vertically aligned with button, the robot should move gripper to above button.
    - When the robot's gripper is vertically aligned with button and the robot's gripper is not near button, the robot should press down on button.


'''

tasks_info = []
tasks_info.append(
    ('window-close',
    '''
To slide the window closed to the right reliably, the robot should perform the following steps:
    - When the window handle is right of the robot's gripper and the robot's gripper is not near the window handle, the robot should move gripper to left of window handle.
    - When the robot's gripper is near the window handle, the robot should slide window right.
    - When the robot's gripper is in front of the window handle, the robot should push window right harder.
''',
    ('vertically',),
    ('above',),
))

tasks_info.append(
    ('window-open',
    '''
To slide the window open to the left reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle, the robot should move gripper to right of window handle.
    - When the robot's gripper is near the window handle, the robot should slide window left.
    - When the robot's gripper is in front of the window handle, the robot should push window left harder.
''',
    ('vertically',),
    ('above',),
))

tasks