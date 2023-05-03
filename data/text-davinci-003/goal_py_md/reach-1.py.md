

This task requires the robot to reach the target location without touching or grabbing any objects. 

# reach: reach to the target location
def reach(robot):
    # Steps:
    #  1. Move gripper towards the target location
    # First, move the gripper towards the target location. 
    if check("the robot's gripper is not close to the target location"):
        robot.move_gripper("close to the target location")
    # Once the gripper is close to the target, move it to the target's exact coordinates. 
    if check("the robot's gripper is not at the target location"):
        robot.move_gripper("at the target location")