
    Steps: 1. Put gripper above the block  2. Drop gripper around the block  3. Close gripper around the block  4. Move block to goal
    Move the robot's gripper until the robot's gripper is above the block

The task `reach-side-left` requires the robot to slide its gripper to the target location from the left.
To slide its gripper to the target location from the left reliably, the robot should perform the following steps:
    Steps: 1. Move towards the target  2. Reach the target
    Move the robot's gripper until the robot's gripper is below the target location

The task `shelf-remove` requires the robot to pick up the block and move it to the target location.
To pick up the block and move it to the target location reliably, the robot should perform the following steps:
    Steps: 1. Put gripper above the block  2. Drop gripper around the block  3. Close gripper around the block  4. Move block to goal
    Move the robot's gripper until the robot's gripper is near the target location

The task `push-side` requires the robot to slide the puck to the target location.
To slide the puck to the target location reliably, what steps the robot should perform?
    Steps:  1. Put gripper in front of the puck  2. Line up gripper sideways  3. Slide the puck to the goal
    First, put the gripper in front of the puck so that we don't bump the puck while trying to slide it.
    - When the robot's gripper is not horizontally aligned with the puck and the robot's gripper is not in front of the puck, move the robot's gripper until the robot's gripper is horizontally aligned with the puck
    If the gripper is in front of the puck and the puck is below the gripper, we can move the gripper to slide the puck.
    - When the puck is below the robot's gripper and the robot's gripper is in front of the puck, move the robot's gripper until the robot's gripper is left of the target location
    If the puck is not below the gripper, we need to line the gripper up sideways to slide the puck.
    - When the robot's gripper is left of the puck and the puck is not below the robot's gripper, move the robot's gripper until the robot's gripper is horizontally aligned with the puck and the robot's gripper is open

The task `push-front` requires the robot to slide the puck to