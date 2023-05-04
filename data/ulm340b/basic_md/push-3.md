
    - When the robot's gripper is not near the puck, the robot should place gripper near puck.
    - When the robot's gripper is near the puck, the robot should push puck to goal.

The task `slide-window-left` requires the robot to slide the window left to open the window.
To slide the window left to open the window reliably, what steps the robot should perform?
    - When the robot's gripper is not near the window handle, the robot should place gripper near window handle.
    - When the robot's gripper is near the window handle, the robot should slide window left.
    - When the robot's gripper is in front of the window handle, the robot should push window left harder.

The task `block-reach` requires the robot to reach to the top of the block.
To reach to the top of the block reliably, what steps the robot should perform?
    - When the robot's gripper is not above the block, the robot should place gripper above block.
    - When the robot's gripper is not near block, the robot should place gripper near block.

The task `slide-window-right` requires the robot to slide the window to the right.
To slide the window to the right reliably, what steps the robot should perform?
    - When the window handle is right of the robot's gripper and the robot's gripper is not near the window handle, the robot should move gripper to left of window handle.
    - When the robot's gripper is near the window handle, the robot should slide window right.
    - When the robot's gripper is in front of the window handle, the robot should push window right harder.

"""

INSTRUCTIONS_BUTTONPRESSTOPDOWN_NODEBUG = "Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects. \n\nPress the button down from above. Press `a` to make the robot step forward and press `d` to make the robot step backwards."

INSTRUCTIONS_DRAWEROPEN_NODEBUG = "Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects. \n\nPull the drawer open. Press `a` to make the robot step forward and press `d` to make the robot step backwards."

INSTRUCTIONS_PEGINSERTSIDE_NODEBUG = "Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects. \n\nGrab the peg and insert it into the hole from the side. Press