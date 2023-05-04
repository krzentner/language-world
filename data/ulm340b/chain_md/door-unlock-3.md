

The task `pick-place-side` requires the robot to grab the puck from the side and hold it at the target location.
To grab the puck from the side and hold it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Line up the robot's gripper with the puck as seen from in front  2. Line up the robot's gripper above the puck  3. Grab the puck from the side  4. Move the puck to the goal
    First, put the gripper above the puck.
    - When the robot's gripper is not forward aligned with puck and the robot's gripper is not above the puck, the robot should put gripper above puck.
    If the gripper is above the puck, check if the gripper is lined up horizontally.
    - When the robot's gripper is above the puck and the robot's gripper is not horizontally aligned with puck, the robot should align gripper with puck.
    If the gripper is lined up with the puck as seen from in front, and it is open, we can close the gripper to grab the puck from the side.
    - When the robot's gripper is horizontally aligned with puck and the robot's gripper is open, the robot should grab puck from side.
    If the robot's gripper is closed and around the puck, we can probably hold the puck at the goal.
    - When the robot's gripper is near puck and the robot's gripper is closed, the robot should move puck to goal.

The task `pick-place-topdown` requires the robot to grab the puck and hold it at the target location.
To grab the puck and hold it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Drop gripper around puck  3. Close gripper around puck  4. Move puck to goal
    First, put the gripper above puck, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the puck, the robot should place gripper above puck.
    If the gripper isn't around the puck, put it around the puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, the robot should drop gripper around puck.
    If the gripper is near the puck and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near puck and the robot's gripper is open, the