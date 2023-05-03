
    if check("the robot's gripper is not above the box lid"):
        robot.place("gripper above box lid")
    if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
        robot.drop("gripper around box lid")
    if check("the robot's gripper is forward aligned with the box lid"):
        robot.move("gripper around box to top of box")
    if check("the robot's gripper is above the box lid and the robot's gripper is open"):
        robot.close("gripper around box lid")