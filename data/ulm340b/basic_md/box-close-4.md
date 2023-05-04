:
    - When the robot's gripper is not above the box lid, the robot should place gripper above box lid.
    - When the robot's gripper is not around the box lid and the robot's gripper is open, the robot should drop gripper around box lid.
    - When the robot's gripper is near the box lid and the robot's gripper is open, the robot should close gripper around box lid.
    - When the robot's gripper is above the box lid and the robot's gripper is closed, the robot should place box lid above box.
"""

instruction_text_long = """


Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

The task `door-open` requires the robot to pull the door open.
To pull the door open reliably, the robot should perform the following steps:
    - When the robot's gripper is not almost vertically aligned with door handle, the robot should put gripper above door handle.
    - When the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open, the robot should put gripper around door handle.
    - When the robot's gripper is vertically aligned with the door handle, the robot should pull door open.
    - To put gripper above door handle, the robot should reach to point above handle.
    - To put gripper around door handle, the robot should move gripper toward door handle until gripper touches door handle.
    - To pull door open, the robot should move gripper away from the door.

The task `reach` requires the robot to reach to the target location.
To reach to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not near reach target, the robot should reach to goal.
    - To reach to goal, the robot should move gripper to a point above the target.

The task `window-close` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, the robot should perform the following steps:
    - When the window handle is right of the robot's gripper and the robot's gripper is not near the window handle, the robot should move gripper to left of window handle.
    - When the robot's gripper is near the window handle, the robot should slide window right.
    - When the robot's gripper is in front of the window handle, the robot should push window right harder.
    - To move gripper to left of window handle, the robot should push gripper left.
