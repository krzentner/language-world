# reach: reach to the target location
def reach(robot):
    if check("the robot's gripper is not near reach target"): # check if the gripper is not already at the target
        robot.reach("to goal") # move the gripper to the target location