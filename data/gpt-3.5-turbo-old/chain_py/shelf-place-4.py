# Steps:
#  1. Put gripper above block
#  2. Grab the block with the gripper
#  3. Move gripper to target location
#  4. Release the block
# First, put the gripper roughly above the block
if check("the robot's gripper is not above the block"):
    robot.place("gripper above block")
# If the gripper is above the block, grab the block with the gripper
if check("the robot's gripper is above the block and the robot's gripper is open"):
    robot.grab("block with gripper")
# If the gripper is holding the block, move the gripper to the target location
if check("the robot's gripper is holding the block and the robot is not at the target location"):
    robot.move("gripper to target location")
# If the gripper is at the target location, release the block
if check("the robot's gripper is at the target location"):
    robot.release("block at target location")