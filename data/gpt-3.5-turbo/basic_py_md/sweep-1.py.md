# sweep: grab the cube and move it sideways to the target location
# def sweep(robot):
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.lift("the cube off the table")
    if check("the robot is not sideways aligned with the target location"):
        robot.move("to the side of the target location")
    if check("the robot is sideways aligned with the target location"):
        robot.push("the cube to the target location")