# reach: reach to the target location
# def reach(robot):
def reach(robot):
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")