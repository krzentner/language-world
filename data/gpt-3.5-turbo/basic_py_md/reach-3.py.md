# reach: reach to the target location
def reach(robot):
    if check("the robot's gripper is not near the target location"):
        robot.move("gripper to target location")
    if check("the robot's gripper is near the target location and the robot's gripper is closed"):
        robot.release("object at target location")