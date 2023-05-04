
"""

TEMPLATE_INTRO_3 = """Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.


The task `reach` requires the robot to reach to the target location.
To reach to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not near reach target, the robot should reach to goal.

The task `push` requires the robot to slide the puck to the target location.
To slide the puck to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should push the gripper into the puck.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should slide the puck to the goal.

The task `window-close` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, the robot should perform the following steps:
    - When the window handle is right of the robot's gripper and the robot's gripper is not near the window handle, the robot should move gripper to left of window handle.
    - When the robot's gripper is near the window handle, the robot should slide window right.
    - When the robot's gripper is in front of the window handle, the robot should push window right harder.

The task `window-open` requires the robot to slide the window open to the left.
To slide the window open to the left reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle, the robot should move gripper to right of window handle.
    - When the robot's gripper is near the window handle, the robot should slide window left.
    - When the robot's gripper is in front of the window handle, the robot should push window left harder.

The task `drawer-close` requires the robot to push the drawer close.
To push the drawer close reliably, the robot should perform the following steps:
    - When the robot's gripper is not near the drawer handle, the robot should grab drawer handle.
    - When the robot's gripper is forward aligned with drawer handle, the robot should push drawer closed.

