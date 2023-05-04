
    Steps:  1. Align the robot's gripper so it's above the button  2. Insert the gripper into the space over the wall  3. Push the button from above
    Because the wall is short, we can just ignore the wall and go over it.
    - When the robot's gripper is not above button and the robot's gripper is not vertically aligned with button, move the robot's gripper until the robot's gripper is vertically aligned with the button and the robot's gripper is closed
    Because we are going above the wall, we should make sure we don't bump it.
    - When the robot's gripper is near the wall and the robot's gripper is vertically aligned with the button, move the robot's gripper until the robot's gripper is above the button
    Once we are above the wall, we can push down on the button.
    - When the robot's gripper is above the button and the robot's gripper is not near the button, move the robot's gripper until the robot's gripper is near the button


The task `drawer-close` requires the robot to push the drawer closed.
To push the drawer closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper roughly around the drawer handle  2. Push the drawer closed
    If the gripper is not near the drawer handle, move it to the drawer handle. We don't need to be careful about the direction, since the drawer is large and we're just pushing it (unlike when opening the drawer).
    - When the robot's gripper is not near the drawer handle, move the robot's gripper until the robot's gripper is near the drawer handle
    If the drawer is aligned with the gripper as seen from in front, we can push the drawer closed.
    - When the robot's gripper is forward aligned with drawer handle, move the robot's gripper until the robot's gripper is around the drawer handle

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper roughly around the door handle  2. Push the door closed
    If the gripper is not near the door handle, move it to the door handle.
    - When the robot's gripper is not near the door handle, move the robot's gripper until the robot's gripper is near the door handle
    If the drawer is aligned with the gripper as seen from in