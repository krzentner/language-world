The task `coffee-push` can be divided into two sub-tasks: `grab` and `move`
 
For the `grab` sub-task, the robot should perform the following steps:
    Steps: 1. Put gripper above mug  2. Grab the handle of the mug  3. Lift the mug up
    First, put the gripper above the mug.
    - When the robot's gripper is not vertically aligned with the mug, the robot should put gripper above mug.
    If the gripper is already above the mug, try to grab the handle of the mug.
    - When the robot's gripper is above the mug and the robot's gripper is not around the handle, the robot should grab mug handle.
    If the gripper successfully grabs the handle of the mug, lift the mug up.
    - When the robot's gripper is holding the mug handle, the robot should lift the mug up.
    
For the `move` sub-task, the robot should perform the following steps:
    Steps: 1. Move to the target location  2. Release the mug
    Move the gripper and mug to the target location while keeping the mug above the surface.
    - When the mug is not above target location, the robot should move to the target location while holding the mug.
    When the target location is reached, release the mug.
    - When the robot's gripper is at the target location, the robot should release the mug.