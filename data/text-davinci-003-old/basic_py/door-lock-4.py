
    if check("the robot's gripper is not above the door handle and the door handle is not twisted"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is above the door handle and the door handle is not twisted"):
        robot.grab("door handle")
    if check("the door handle is twisted"):
        robot.turn("door handle clockwise")