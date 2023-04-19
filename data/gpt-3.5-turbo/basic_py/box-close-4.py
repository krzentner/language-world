if check("the robot's gripper is not above the box lid"):
        robot.place("gripper above box lid")
    if check("the robot's gripper is not around box lid and the robot's gripper is open"):
        robot.drop("gripper around box lid")
    if check("the robot's gripper is near box lid and the robot's gripper is open"):
        robot.close("gripper around box lid")
    if check("the robot's gripper is above box and the robot's gripper is closed"):
        robot.place("box lid on top of box")