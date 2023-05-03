
    if check("the robot's gripper is not near cup"):
        robot.reach("grab cup")
    if check("the robot's gripper is near cup and the cup is below the robot's gripper"):
        robot.grab("cup")
    if check(" the robot's gripper is holding cup and the target location is not near robot"):
        robot.pull("cup to goal")