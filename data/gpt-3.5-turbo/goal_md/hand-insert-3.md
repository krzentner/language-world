It's not clear what "hand-insert" means in this context. Assuming you meant "pick-and-place", similar to the "pick-place" task mentioned earlier, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Drop gripper around puck  3. Close gripper around puck  4. Move puck to target location
    First, put the gripper roughly above the puck so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the puck, move the robot's gripper until the robot's gripper is above the puck
    If the gripper isn't around the puck, put it around the puck.
    - When the robot's gripper is not around the puck and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the puck and the robot's gripper is closed
    If the gripper is near the puck and closed, we've probably grabbed it. Move the puck to the target location.
    - When the robot's gripper is closed around the puck, move the robot's gripper until the puck is above the target location