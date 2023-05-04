
'''

# Answer:
# - When the robot's gripper is not near the handle, the robot should put gripper above handle.
# - When the robot's gripper is near the handle, the robot should press down on handle.
# - When the robot's gripper is forward aligned with handle, the robot should release handle.

'''
The task `peg-insert-side-wall` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    - When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, the robot should align peg to hole.
    - When peg is horizontally aligned with hole, the robot should insert peg into hole.
'''

'''
The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    - When the robot's gripper is not almost vertically aligned with the door handle and the robot's gripper is open, the robot should put gripper around the door handle.
    - When the robot's gripper is almost vertically aligned with the door handle, the robot should push door closed.
'''


'''
The task `window-close-wall` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, the robot should perform the following steps:
    - When the window handle is right of the robot's gripper and the robot's gripper is not near the window handle, the robot should move gripper to left of window handle.
    - When the robot's gripper is near the window handle, the robot should slide window right.
    - When the robot's gripper is in front of the window handle, the robot should push window right harder.
'''


'''
The task `drawer-close-wall` requires the robot to push the drawer closed.
To push the drawer closed reliably, the robot should perform the following steps:
    - When the robot's gripper is not near the drawer handle, the robot should grab drawer handle.
    - When the robot's gripper is forward aligned with drawer handle, the robot should push drawer closed.
'''


'''
The task `peg-unplug-side` requires the robot to