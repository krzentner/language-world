
Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.


The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top
    Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    Now that the gripper is lined up, just push down on the button.
    - When the robot's gripper is vertically aligned with button, the robot should push down on button.

The task `drawer-open` requires the robot to pull the drawer open.
To pull the drawer open reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above drawer handle  2. Drop gripper around drawer handle  3. Pull open the drawer
    We need to put the gripper above the drawer handle before we can grab it, because of the angle of the robot's gripper.
    - When the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer handle.
    Once the gripper is lined up above the drawer handle, we should be able to grab the drawer handle by moving the gripper down around it.
    - When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, the robot should put gripper around drawer handle.
    Once the gripper is around the drawer handle, we can just pull the drawer open.
    - When the robot's gripper is around drawer handle, the robot should pull away from drawer.

The task `drawer-close` requires the robot to push the drawer close.
To push the drawer close reliably, the robot should perform the following steps:
    Steps:  1. Put gripper roughly around the drawer handle  2. Push the drawer closed
    If the gripper is not near the drawer handle, move it to the drawer handle. We don't need to be careful about the direction, since the drawer is large and we're just pushing it (unlike when opening the drawer).
    - When the robot's gripper is not near the drawer handle, the robot should grab drawer handle.
    If the drawer is aligned with the gripper as