if check("the robot's gripper is not above the mug"):
        robot.place("gripper above mug")
    if check("the robot's gripper is not around the mug and the robot's gripper is open"):
        robot.drop("gripper around mug")
    if check("the robot's gripper is near mug and the robot's gripper is open"):
        robot.close("gripper around mug")
    if check("the mug is in the robot's gripper and the robot's gripper is not near the target location"):
        robot.move("the mug to the target location")
    if check("the mug is in the robot's gripper and the robot's gripper is near the target location"):
        robot.slide("the mug to the target location")