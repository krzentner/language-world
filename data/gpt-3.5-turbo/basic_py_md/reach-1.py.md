# reach: reach to the target location
def reach(robot):
    if check("the robot's gripper is not near the target location"):
        robot.move("the gripper to the target location")
    if check("the robot's gripper is near the target location"):
        robot.grab("the object at the target location")