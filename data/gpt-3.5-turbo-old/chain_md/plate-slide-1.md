The robot should perform the following steps:
    Steps:  1. Put gripper above plate  2. Push gripper into plate  3. Slide plate to goal
    First, put the gripper above the plate.
    - When the robot's gripper is not above the plate, the robot should place gripper above plate.
    If the gripper is not pressed against the plate, move the gripper down to the plate to slide it.
    - When the robot's gripper is above the plate and the gripper is not pressed against the plate, the robot should push the gripper into the plate.
    If the gripper is near the goal, we've probably trapped the plate and can slide it to the target location. Close the gripper to make sure that we keep control of the plate.
    - When the robot's gripper is near the plate and the plate is below the robot's gripper, the robot should slide the plate to the goal.