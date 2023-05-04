
    Steps:  1. Put gripper above mug  2. Drop gripper around mug  3. Slide mug to goal
    First, we need to put the gripper above the mug.
    - When the robot's gripper is not vertically aligned with mug, the robot should put gripper above mug.
    If the gripper is vertically aligned with the mug but not around it, we can put it around the mug to grab it.
    - When the robot's gripper is vertically aligned with mug and the robot's gripper is open, the robot should drop gripper around mug.
    Once we've grabbed the mug we can slide it to the goal.
    - When the robot's gripper is around mug, the robot should slide mug to goal.

The task `sweep-into` requires the robot to push the puck into the trash bin.
To push the puck into the trash bin reliably, what steps the robot should perform?
    Steps:  1. Put gripper above puck  2. Push gripper into top of puck  3. Slide puck into trash bin
    The robot can slide the puck by trapping it by pushing down on it from above and moving the gripper. If the puck isn't below the gripper as seen from above, move the gripper above the puck.
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
    If the gripper is aligned with the puck but not near it, move the gripper down to the puck to slide it.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should push the gripper into the puck.
    If the gripper is near the puck, we've probably trapped the puck and can slide it to the trash bin. Close the gripper to make sure we keep control of the puck.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should slide the puck to the trash bin.

The task `plate-slide` requires the robot to grab the plate and slide it to the target location.
To grab the plate and slide it to the target location reliably, what steps the robot should perform?
    Steps:  1. Put gripper above plate  2. Drop gripper around plate  3. Slide plate to goal
    First, we need to put the gripper above the plate.
    - When the robot's gripper is not vertically aligned with plate, the robot should