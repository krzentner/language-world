# reach: reach to the target location
def reach(robot):
    # Steps:
    #  1. Move gripper to the target location
    # Move the gripper to the target location to "reach" it.
    if check("the robot's gripper is not at the target location"):
        robot.move("gripper to target location")