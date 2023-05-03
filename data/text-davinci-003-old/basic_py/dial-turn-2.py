
    if check("the robot's gripper is not close to the dial"):
        robot.reach("dial")
    if check("the robot's gripper is close to the dial"):
        robot.turn("dial to goal")
    if check("the robot's gripper is still close to the dial"):
        robot.push("dial harder")