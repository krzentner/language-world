# push: slide the puck to the target location
def push(robot):
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is around the puck"):
        robot.slide("puck to goal")