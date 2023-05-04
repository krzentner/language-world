1. ... 2. ...
    Hello. You didn't answer in a while. I'll give the full explanation now.
    Steps:  1. Put gripper above puck  2. Push gripper into top of puck  3. Slide puck to goal  4. Line gripper up to target
    The robot can pick up the puck by trapping it by pushing down on it from above and moving the gripper. If the puck isn't below the gripper as seen from above, move the gripper above the puck.
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, move the robot's gripper until the robot's gripper is vertically aligned with the puck
    If the gripper is aligned with the puck but not near it, move the gripper down to the puck to pick it up.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, move the robot's gripper until the robot's gripper is above the puck and the robot's gripper is closed
    Now that the puck is in the robot's gripper, we can move to the target location. Because the target is a location in space, we should line up the gripper with it as seen from above.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, move the robot's gripper until the robot's gripper is above the target location

The task `drawer-close` requires the robot to push the drawer closed.
To push the drawer closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper roughly around the drawer handle  2. Push the drawer closed
    If the gripper is not near the drawer handle, move it to the drawer handle. We don't need to be careful about the direction, since the drawer is large and we're just pushing it (unlike when opening the drawer).
    - When the robot's gripper is not near the drawer handle, move the robot's gripper until the robot's gripper is near the drawer handle
    If the drawer is aligned with the gripper as seen from in front, we can push the drawer closed.
    - When the robot's gripper is forward aligned with drawer handle, move the robot's gripper until the robot's gripper is around the drawer handle

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    Steps: 