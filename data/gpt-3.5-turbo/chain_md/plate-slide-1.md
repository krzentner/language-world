The robot can slide the plate by pushing it from above and moving the gripper. To reliably slide the plate into the target location, the robot should perform the following steps:
    Steps:  1. Put gripper above the plate  2. Push gripper into top of plate  3. Slide plate to goal
    If the plate is not below the gripper as seen from above, move the gripper above the plate.
    - When the robot's gripper is not above the plate and the robot's gripper is not vertically aligned with the plate, the robot should put the gripper above the plate.
    If the gripper is aligned with the plate but not near it, move the gripper down to the plate to slide it.
    - When the robot's gripper is vertically aligned with the plate and the robot's gripper is not near the plate, the robot should push the gripper into the plate.
    If the gripper is near the plate, we've probably trapped the plate and can slide it to the target location. Close the gripper to make sure we keep control of the plate.
    - When the robot's gripper is near the plate and the plate is below the robot's gripper, the robot should slide the plate to the goal.