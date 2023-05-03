# reach: reach to the target location
def reach(robot):
    if check("the robot's gripper is not above the target location"):
        robot.move("gripper above target location")
    if check("the robot's gripper is above the target location and the robot's gripper is not too far away from it"):
        robot.grab("the target")
    if check("the robot's gripper is carrying the target and the robot's gripper is not above the destination"):
        robot.move("gripper above destination")
    if check("the robot's gripper is above the destination"):
        robot.release("the target")