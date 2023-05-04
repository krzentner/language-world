
    Steps:
    - When the coffee machine's button is not near the robot's gripper, the robot should move the gripper near the button.
    - When the coffee machine's button is near the robot's gripper, the robot should push the button.

The task `drawer-close-side` requires the robot to slide the drawer close to the right.
To slide the drawer close to the right reliably, the robot should perform the following steps:
    Steps:  1. Put gripper left of the drawer handle  2. Start pushing against the drawer handle to close the drawer  3. Push the drawer closed harder
    If the the drawer handle is right of the robot's gripper, we should move the gripper near the drawer handle to start pushing
    - When the drawer handle is right of the robot's gripper and the robot's gripper is not near the drawer handle, the robot should move gripper to left of drawer handle.
    If the robot's gripper is near the drawer handle we can probably slide the drawer close now by moving the gripper right.
    - When the robot's gripper is near the drawer handle, the robot should slide drawer right.
    If the robot's gripper is starting to be in front of the drawer handle, push harder.
    - When the robot's gripper is in front of the drawer handle, the robot should push drawer right harder.

The task `drawer-open-side` requires the robot to pull the drawer open.
To pull the drawer open reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above drawer handle  2. Drop gripper around drawer handle  3. Pull open the drawer
    First, put the gripper above the drawer handle.
    - When the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer handle.
    Once the gripper is lined up above the drawer handle, we should be able to grab the drawer handle by moving the gripper down around it.
    - When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, the robot should put gripper around drawer handle.
    Once the gripper is around the drawer handle, we can just pull the drawer open.
    - When the robot's gripper is around drawer handle, the robot should pull away from drawer.

The task `button-press` requires the robot to push the button.
To push the button reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper horizontally in front of the