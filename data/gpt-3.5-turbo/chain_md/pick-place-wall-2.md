To pick up the puck and hold it at the target location with a short wall in the way reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the puck  2. Drop gripper around the puck  3. Close gripper around the puck  4. Move the puck above the wall  5. Move the gripper to the goal location  6. Release the puck
    First, put the gripper roughly above the puck, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the puck, the robot should place gripper above puck.
    If the gripper isn't around the puck, put it around the puck.
    - When the robot's gripper is not around the puck and the robot's gripper is open, the robot should drop gripper around puck.
    If the gripper is near the puck and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near the puck and the robot's gripper is open, the robot should close gripper around puck.
    We closed the gripper, and the puck is still near the gripper, so maybe we grabbed it. We can move the gripper up and over the wall to the goal location.
    - When the robot's gripper is closed and the puck is still below the height of the wall, the robot should move the gripper up over the wall.
    Once the gripper and puck are above the wall, we can move the gripper to the goal location.
    - When the robot's gripper and puck are above the wall, the robot should move gripper to goal location.
    Finally, we can release the puck at the goal location.
    - When the robot's gripper is at the goal location and the gripper is closed around the puck, the robot should release the puck.