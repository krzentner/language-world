
    Steps:  1. Move the robot end-effector towards the target location  2. Slowly move the robot's end-effector until close enough to the target location  3. Stop movement when the robot's end-effector is close enough to the target location
    The task of reach basically involves moving the robot's end-effector towards the target location. Picking something up does not matter.
    - When the robot's end-effector is not close enough to the target location, move the robot's end-effector towards the target location
    When the end-effector is close enough to the target location, the robot should slow down the movement of the end-effector, since the task is to reach and not to hit.
    - When the robot's end-effector is close enough to the target location, move the robot's end-effector until the end-effector stops moving when it is close enough to the target location