# reach: reach to the target location
def reach(robot):
    if check("the robot's gripper is not above the target location"):
        robot.put("gripper above target")
    if check("the robot's gripper is not near the target location"):
        robot.move("gripper to target")
    if check("the robot's gripper is near the target location"):
        robot.grab("target")
        robot.move("gripper up")
    if check("the robot's gripper is above the target location"):
        robot.drop("gripper")