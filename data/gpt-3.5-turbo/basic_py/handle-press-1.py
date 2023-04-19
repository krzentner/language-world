    if check("the robot's gripper is not above the handle"):
        robot.place("gripper above handle")
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    if check("the robot's gripper is near handle and the robot's gripper is open"):
        robot.close("gripper around handle")
    if check("the robot's gripper is above handle and the robot's gripper is closed"):
        robot.push("down on handle")