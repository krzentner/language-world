if check("the robot's gripper is not above the mug"):
        robot.place("gripper above the mug")
    if check("the robot's gripper is not around the mug and the robot's gripper is open"):
        robot.drop("gripper around the mug")
    if check("the robot's gripper is near the mug and the robot's gripper is open"):
        robot.close("gripper around the mug")
    if check("the robot's gripper is above the mug and the robot's gripper is closed"):
        robot.move("the mug to the target location")