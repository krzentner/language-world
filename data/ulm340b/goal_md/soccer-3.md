
    - When the ball is not near the target location, move the robot's gripper until the ball is in front of the robot's gripper
    - When the robot's gripper is above the ball, move the robot's gripper until the ball is near the target location

The task `peg-unstack` requires the robot to grab the peg and unstack it.
To grab the peg and unstack it reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above peg  2. Grab the peg with the gripper  3. Lift the peg up away from the stack
    As long as the peg is not above the gripper, move the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, move the robot's gripper until the robot's gripper is vertically aligned with the peg
    Since the gripper is above the peg, we can grab it by closing the gripper.
    - When the robot's gripper is vertically aligned with the peg, move the robot's gripper until the robot's gripper is forward aligned with the peg
    As long as the gripper is still forward aligned with the peg, lift the gripper to unstack it.
    - When the robot's gripper is forward aligned with the peg, move the robot's gripper until the robot's gripper is above the peg

The task `drawer-stack` requires the robot to stack the drawer on top of the drawer stack.
To stack the drawer on top of the drawer stack reliably, the robot should perform the following steps:
    Steps:  1. Move the drawer to roughly above the stack  2. Move the drawer directly above the stack  3. Drop the drawer onto the stack
    As long as the drawer stack is not roughly in front of the gripper, move the gripper to roughly above the drawer stack.
    - When the robot's gripper is not in front of the drawer stack, move the robot's gripper until the robot's gripper is near the drawer stack
    As long as the gripper is not directly above the drawer stack, move the gripper towards directly above the drawer stack.
    - When the robot's gripper is in front of the drawer stack, move the robot's gripper until the robot's gripper is above the drawer stack
    As long as the gripper is above the drawer stack, move the gripper down to drop the drawer onto the drawer stack.
    - When the robot's gripper is above the drawer stack, move the robot's gripper until the robot's gripper