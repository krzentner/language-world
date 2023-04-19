# sweep-into: grab the cube and move it to the target location
# def sweep_into(robot):
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above the cube")
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.drop("gripper around the cube")
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.close("gripper around the cube")
    if check("the robot's gripper is above the cube and the robot's gripper is closed"):
        robot.pull("the cube towards itself")
    if check("the robot's gripper is above the target location"):
        robot.push("the cube onto the target location")