
    Steps:  1. Move gripper toward the drawer handle  2. Line up the gripper with the drawer handle  3. Close the drawer

The task `door-close` requires the robot to push the door close.
To push the door close reliably, what steps the robot should perform?
    Steps:  1. Move gripper toward the door handle  2. Line up the gripper with the door handle  3. Close the door

The task `pick-place` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Drop gripper around puck  3. Close gripper around puck  4. Move puck to goal
    First, put the gripper roughly above puck, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the puck, move the robot's gripper until the robot's gripper is above the puck
    If the gripper isn't around the puck, put it around the puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the puck and the robot's gripper is closed
    If the gripper is near the puck and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is above puck and the robot's gripper is closed, move the robot's gripper until the robot's gripper is near the target location

The task `push` requires the robot to slide the puck to the target location.
To slide the puck to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Push gripper into top of puck  3. Slide puck to goal
    The robot can slide the puck by trapping it by pushing down on it from above and moving the gripper. If the puck isn't below the gripper as seen from above, move the gripper above the puck.
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, move the robot's gripper until the robot's gripper is vertically aligned with the puck
    If the gripper is aligned with the puck but not near it, move the gripper down to the puck to slide it.
    - When the robot's gripper