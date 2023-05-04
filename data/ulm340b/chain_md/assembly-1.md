
    Steps:  1. Move robot's gripper to the wrench  2. Close robot's gripper around the wrench  3. Pick up the wrench  4. Move wrench to peg  5. Put wrench around peg
    First, put the gripper above the wrench.
    - When the robot's gripper is not above the wrench, the robot should move gripper to wrench.
    If the gripper isn't around the wrench, put it around the wrench.
    - When the robot's gripper is not around wrench and the robot's gripper is open, the robot should drop gripper around wrench.
    If the gripper is near the wrench and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near wrench and the robot's gripper is open, the robot should close gripper around wrench.
    We closed the gripper, and the wrench is still near the gripper, so maybe we grabbed it. Try to move the wrench to the peg. If we didn't grab it, we'll just go back to an earlier step.
    - When the robot's gripper is near wrench and the robot's gripper is closed, the robot should move wrench to peg.
    Once the wrench is near the peg, move it around the peg.
    - When the robot's gripper is near peg, the robot should move gripper to encircle peg.

The task `stack-up` requires the robot to move the block on top of the peg.
To move the block on top of the peg reliably, the robot should perform the following steps:
    Steps:  1. Move gripper above the block  2. Lower gripper around block  3. Grab block  4. Lift block up  5. Slide block on top of peg
    As long as the gripper isn't above the block, move it towards the block to pick it up.
    - When the robot's gripper is not above block, the robot should move gripper above block.
    If the block is below the robot's gripper, lower the gripper around the block.
    - When the block is below the robot's gripper, the robot should lower gripper around block.
    Now that the gripper is around the block, close it to grab the block.
    - When the block is around the robot's gripper and the robot's gripper is open, the robot should close gripper around block.
    We closed the gripper, and the block is still near the gripper, so maybe we grabbed it. If