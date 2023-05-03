The task `coffee-push` requires the robot to grab the mug and move it to the target location. To do this reliably, the robot should perform the following steps:

    Steps:  1. Put gripper above handle of the mug
            2. Drop gripper around the handle of the mug
            3. Close gripper around the handle of the mug
            4. Move the gripper and mug to the target location
            5. Open the gripper to release the mug at the target location

First, put the gripper above the handle of the mug.
    - When the robot's gripper is not above the handle of the mug, move the robot's gripper until the robot's gripper is above the handle of the mug
If the gripper is not around the handle of the mug, drop it around the handle of the mug.
    - When the robot's gripper is not around the handle of the mug and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the handle of the mug and the robot's gripper is closed
If the gripper is around the handle of the mug, move the gripper and mug to the target location.
    - When the robot's gripper is holding the mug and the robot's gripper is not above the target location, move the robot's gripper until the robot's gripper is above the target location
Once the gripper is above the target location, release the mug by opening the gripper.
    - When the robot's gripper is above the target location and the robot's gripper is closed around the handle of the mug, open the gripper to release the mug at the target location.