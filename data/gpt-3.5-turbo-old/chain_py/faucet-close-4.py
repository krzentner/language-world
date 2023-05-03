# Steps:
#  1. Move gripper to right of faucet handle
#  2. Grip the faucet handle
#  3. Turn the handle right to close the faucet
# First, we need to move the gripper to the right of the faucet handle.
if check("the robot's gripper is not to the right of the faucet handle"):
    robot.move("the gripper to the right of the faucet handle")
# Once we're lined up with the handle, we can grip it.
if check("the robot's gripper is to the right of the faucet handle and the robot's gripper is not gripping the faucet handle"):
    robot.grip("the faucet handle")
# Finally, we turn the handle right to close the faucet.
if check("the robot's gripper is gripping the faucet handle"):
    robot.turn("the faucet handle right to close it")