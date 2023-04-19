if check("the robot's gripper is not above the lid of the box"):
        robot.place("gripper above lid of the box")
    if check("the robot's gripper is not around the lid of the box and the robot's gripper is open"):
        robot.drop("gripper around lid of the box")
    if check("the robot's gripper is near the lid of the box and the robot's gripper is open"):
        robot.close("gripper around lid of the box")
    if check("the robot's gripper is above the box and the robot's gripper is closed"):
        robot.place("lid of the box on the box")