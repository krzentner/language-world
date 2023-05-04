
    - When the robot's gripper is above the cube, the robot should drop gripper around cube.
    - When the robot's gripper is forward aligned with the cube, the robot should grab cube.
    - When the robot's gripper is closed around cube and the cube is not in goal, the robot should slide cube to goal.

The task `block-stack` requires the robot to pick up the cube and place it above another cube.
To pick up the cube and place it above another cube reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the cube, the robot should put gripper above cube.
    - When the robot's gripper is not around cube and the robot's gripper is open, the robot should drop gripper around cube.
    - When the robot's gripper is near cube and the robot's gripper is open, the robot should close gripper around cube.
    - When the robot's gripper is above cube and the robot's gripper is closed, the robot should stack cube on top of another cube.

The task `distractor-block-stack` requires the robot to pick up the blue cube and place it above another cube.
To pick up the blue cube and place it above another cube reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the blue cube, the robot should put gripper above blue cube.
    - When the robot's gripper is not around blue cube and the robot's gripper is open, the robot should drop gripper around blue cube.
    - When the robot's gripper is near blue cube and the robot's gripper is open, the robot should close gripper around blue cube.
    - When the robot's gripper is above blue cube and the robot's gripper is closed, the robot should stack blue cube on top of another cube.

The task `flip-block` requires the robot to flip the block to the specified orientation.
To flip the block to the specified orientation reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the block, the robot should put gripper above block.
    - When the robot's gripper is not around block and the robot's gripper is open, the robot should drop gripper around block.
    - When the robot's gripper is near block and the robot's gripper is open, the robot should close gripper around block.
    - When the robot's gripper is above block and the robot's gripper is closed, the robot should flip block.

The task `rotate-block` requires the