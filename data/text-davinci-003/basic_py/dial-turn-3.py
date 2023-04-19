
    if check("the robot's gripper is not vertically aligned with the dial and the robot's gripper is below the dial"):
        robot.move("gripper to right of dial")
    if check("the robot's gripper is near the dial and the robot's gripper is open"):
        robot.rotate("gripper around dial")
    if check("the robot's gripper is around the dial and the gripper is open"):
        robot.turn("dial clockwise")