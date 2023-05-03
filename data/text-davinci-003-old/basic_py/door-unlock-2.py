
    if check("the robot's gripper is not near the door handle and the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper near door handle")
    if check("the robot's gripper is near door handle and dial is not in desired position"):
        robot.hold("gripper around dial")
    if check("the robot's gripper is not around dial"):
        robot.turn("dial to correct position")