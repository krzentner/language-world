


The task `drawer-close-side` requires the robot to push the drawer closed from the side.
To push the drawer closed from the side reliably, the robot should perform the following steps:
    Steps:  1. Put the gripper roughly above the drawer handle  2. Push closed the drawer
    If the gripper is not near the drawer handle, move it to the drawer handle. We don't need to be careful about the direction, since the drawer is large and we're just pushing it (unlike when opening the drawer).
    - When the robot's gripper is not near drawer handle, the robot should grab drawer handle.
    If the drawer is aligned with the gripper as seen from in front, we can push the drawer closed.
    - When the robot's gripper is forward aligned with drawer handle, the robot should push drawer closed.

The task `drawer-open-side` requires the robot to pull the drawer open from the side.
To pull the drawer open from the side reliably, the robot should perform the following steps:
    Steps:  1. Put the gripper roughly above the drawer handle  2. Open the drawer
    We need to put the gripper above the drawer handle before we can grab it, because of the angle of the robot's gripper.
    - When the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer handle.
    Once the gripper is lined up above the drawer handle, we should be able to grab the drawer handle by moving the gripper down around it.
    - When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, the robot should put gripper around drawer handle.
    Once the gripper is around the drawer handle, we can just pull the drawer open.
    - When the robot's gripper is around drawer handle, the robot should pull away from drawer.

The task `peg-unstack` requires the robot to unstack the peg from the table.
To unstack the peg from the table reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Pick up the peg  3. Move the peg to unstack it
    The robot can't really do anything unless it is near the peg, so put the gripper above the peg.
    - When the robot's gripper is not above the peg, the robot should put gripper above peg.
    Once we are near the peg, we can grab it by dropping the gripper and closing it.
    - When the robot's gripper