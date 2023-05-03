

The task `coffee-push` requires the robot to grab the mug and move it to the target location.
To grab the mug and move it to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not above mug and the robot's gripper is not vertically aligned with the mug, the robot should put the gripper above the mug.
    - When the robot's gripper is vertically aligned with the mug and the robot's gripper is open, the robot should drop the gripper around the mug.
    - When the robot's gripper is around mug and the robot's gripper is open, the robot should close the gripper around the mug.
    - When the robot's gripper is around mug and the robot's gripper is closed, the robot should move the mug to the goal.