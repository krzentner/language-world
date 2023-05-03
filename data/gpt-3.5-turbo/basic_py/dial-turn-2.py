    if check("the robot's gripper is not vertically aligned with dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is vertically aligned with dial and the robot's gripper is not around dial"):
        robot.put("gripper around dial")
    if check("the robot's gripper is around dial and the dial is not in the desired position"):
        robot.turn("dial to the desired position")