""",
    "test": """

##### Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.


The task `button-press-side` requires the robot to push the button in.
To push the button in reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the button, the robot should put gripper above button.
    - When the robot's gripper is vertically aligned with the button, the robot should push button in.

The task `drawer-close` requires the robot to push the drawer close.
To push the drawer close reliably, the robot should perform the following steps:
    - When the robot's gripper is not near the drawer handle, the robot should grab drawer handle.
    - When the robot's gripper is forward aligned with drawer handle, the robot should push drawer closed.

The task `door-open` requires the robot to pull the door open.
To pull the door open reliably, the robot should perform the following steps:
    - When the robot's gripper is not almost vertically aligned with door handle, the robot should put gripper above door handle.
    - When the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open, the robot should put gripper around door handle.
    - When the robot's gripper is vertically aligned with the door handle, the robot should pull door open.

The task `drawer-open` requires the robot to pull the drawer open.
To pull the drawer open reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer handle.
    - When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, the robot should put gripper around drawer handle.
    - When the robot's gripper is around drawer handle, the robot should pull away from drawer.

The task `window-close` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, the robot should perform the following steps:
    - When the window handle is right of the robot's gripper and the robot's gripper is not near the window handle, the robot should move gripper to left of window handle.
    - When the robot's gripper is near the window handle, the robot should slide window right.
    - When the robot's gripper is in front of the window handle, the robot should push window right harder.

The task `window-