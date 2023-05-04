
    The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper from the side  2. Drop gripper around the peg  3. Insert the peg into the hole
    Line up the robot's gripper from the side with the peg.
    - When the robot's gripper is not vertically aligned with the peg, move the robot's gripper until the robot's gripper is vertically aligned with the peg
    If the gripper is aligned with the peg and open, then close the gripper to grab it.
    - When the robot's gripper is aligned with the peg and the robot's gripper is open, move the robot's gripper until the robot's gripper is around the peg and the robot's gripper is closed
    If the gripper is closed and the peg is aligned, we can insert it by moving the gripper toward the target.
    - When the peg is vertically aligned with the robot's gripper, move the robot's gripper until the robot's gripper is near the target location

The task `drawer-close` requires the robot to push the drawer close.
To push the drawer close reliably, the robot should perform the following steps:
    Steps:  1. Put gripper roughly around the drawer handle  2. Push the drawer closed
    If the gripper is not near the drawer handle, move it to the drawer handle. We don't need to be careful about the direction, since the drawer is large and we're just pushing it (unlike when opening the drawer).
    - When the robot's gripper is not near the drawer handle, move the robot's gripper until the robot's gripper is near the drawer handle
    If the drawer is aligned with the gripper as seen from in front, we can push the drawer closed.
    - When the robot's gripper is forward aligned with drawer handle, move the robot's gripper until the robot's gripper is around the drawer handle

The task `pick-place` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Drop gripper around puck  3. Close gripper around puck  4. Move puck to goal
    First, put the gripper roughly above puck, so that we