# reach: reach to the target location
def reach(robot):
# Steps:
#  1. Move the gripper to be at the same height as the target
#  2. Move the gripper to the target location
# To reach to a target, the robot needs to make sure that the gripper is at the correct height
# and location. 
# First, the robot should move the gripper to be at the same height as the target.
    if check("the robot's gripper is not at the same height as the target"):
        robot.move("gripper to target height")
# Once the gripper is at the correct height, move it to the target location.
    if check("the robot's gripper is at the same height as the target and the robot's gripper is not at the target location"):
        robot.move("gripper to target location")