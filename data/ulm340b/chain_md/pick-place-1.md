
    Steps:  1. Put gripper above puck  2. Grab the puck  3. Slide puck to goal
    Because we want to pick the puck up, we need to move the gripper above it so that we can grab the puck.
    - When the robot's gripper is not vertically aligned with the puck, the robot should put gripper above puck.
    If the puck isn't around the robot's gripper yet, we need to grab the puck.
    - When the puck is not around the robot's gripper, the robot should grab puck.
    Now that the puck is being held by the robot's gripper, we can slide it to the goal location.
    - When the robot's gripper is around puck, the robot should slide puck to goal.

The task `pick-place-with-clutter` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the puck  2. Grab the puck  3. Slide the puck to the goal location, while avoiding obstacles
    First, put the gripper above the puck.
    - When the robot's gripper is not vertically aligned with the puck, the robot should put gripper above puck.
    If the puck is not around the robot's gripper yet, we need to grab the puck.
    - When the puck is not around the robot's gripper, the robot should grab puck.
    If the robot's gripper is near the goal but there are obstacles in the way, push the robot's gripper towards the goal.
    - When the robot's gripper is near goal and the robot's gripper is facing obstacles, the robot should push gripper to goal.
    If the robot's gripper is near the goal and not facing obstacles, then it must have a clear path.
    - When the robot's gripper is near goal and the robot's gripper is not facing obstacles, the robot should slide puck to goal.

The task `push-with-clutter` requires the robot to slide the puck to the target location.
To slide the puck to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the puck  2. Push gripper into top of puck  3. Slide the puck to the goal location, while avoiding obstacles
    The robot can slide the puck by trapping it by pushing down on it from above and moving the gripper. If the puck isn'