if check("the robot's gripper is not above the mug"):
        robot.move("gripper above mug")
    if check("the robot's gripper is not around the mug and the robot's gripper is open"):
        robot.drop("gripper around mug")
    if check("the robot's gripper is near mug and the robot's gripper is open"):
        robot.close("gripper around mug")
    if check("the robot's gripper is above mug and the mug is not at the target location"):
        robot.pull("mug to goal")