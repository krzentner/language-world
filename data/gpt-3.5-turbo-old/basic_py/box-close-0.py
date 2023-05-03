if check("the robot's gripper is not above the box lid and the box lid is not on the box"):
        robot.place("gripper above box lid")
    if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
        robot.drop("gripper around box lid")
    if check("the robot's gripper is near the box lid and the robot's gripper is open"):
        robot.close("gripper around box lid")
    if check("the robot's gripper is above the box and the robot's gripper is closed"):
        robot.place("box lid on the box")