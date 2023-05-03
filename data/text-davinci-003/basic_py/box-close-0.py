
    if check("the robot's gripper is not near the box lid"):
        robot.reach("to box lid")
    if check("the robot's gripper is not around box lid and the robot's gripper is open"):
        robot.grab("box lid")
    if check("the robot's gripper is near box lid and the robot's gripper is open"):
        robot.close("gripper around box lid")
    if check("the robot's gripper is above box and the robot's gripper is closed"):
        robot.place("box lid above box")