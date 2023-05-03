
    if check("the robot's gripper is not above the dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is above the dial and the robot's gripper is open"):
        robot.grip("dial")
    if check("the robot's gripper is around the dial"):
        robot.turn("dial")

# final: define a general task for the robot
def final(robot):
    if check("the target is not in reach of the robot"):
        robot.navigate("to the target")
    if check("the robot's gripper is open and the robot is not above the target"):
        robot.place("gripper above target")
    if check("the robot is above the target and the target is not in the robot's gripper"):
        robot.drop("gripper around target")
    if check("the target is in the robot's gripper"):
        robot.place("target to goal")