
    Steps:  1. Put gripper above plate  2. Push gripper into plate  3. Slide plate into the target location
    The robot can slide the plate by pushing down on it from above. If the plate isn't below the gripper as seen from above, move the gripper above the plate.
    - When the robot's gripper is not above plate and the robot's gripper is not vertically aligned with plate, the robot should put the gripper above plate.
    If the gripper is aligned with the plate but not near it, move the gripper down to the plate to slide it.
    - When the robot's gripper is vertically aligned with plate and the robot's gripper is not near plate, the robot should push the gripper into plate.
    If the gripper is near the plate, we've probably trapped the plate and can slide it to the target location. Close the gripper to make sure we keep control of the plate.
    - When the robot's gripper is near plate and the plate is below the robot's gripper, the robot should slide plate into target location.

The task `push-wall` requires the robot to slide the plate towards the wall.
To slide the plate towards the wall reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above plate  2. Push gripper into plate  3. Slide plate towards the wall
    The robot can slide the plate by pushing down on it from above. If the plate isn't below the gripper as seen from above, move the gripper above the plate.
    - When the robot's gripper is not above plate and the robot's gripper is not vertically aligned with plate, the robot should put the gripper above plate.
    If the gripper is aligned with the plate but not near it, move the gripper down to the plate to slide it.
    - When the robot's gripper is vertically aligned with plate and the robot's gripper is not near plate, the robot should push the gripper into plate.
    If the gripper is near the plate, we've probably trapped the plate and can slide it to the wall. Close the gripper to make sure we keep control of the plate.
    - When the robot's gripper is near plate and the plate is below the robot's gripper, the robot should slide plate towards the wall.

The task `pick-orient-place` requires the robot to pick up the puck, rotate it to be flat, and place it on the target location.
To pick up the puck, rotate it to be flat, and place it on the target location