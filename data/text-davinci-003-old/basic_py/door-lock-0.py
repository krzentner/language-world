
    if check("the robot's gripper is not above the lock and the robot's gripper is not vertically aligned with the lock"):
        robot.put("gripper above lock")
    if check("the robot's gripper is vertically aligned with the lock and the robot's gripper is not around the lock"):
        robot.put("gripper around lock")
    if check("the robot's gripper is around the lock"):
        robot.turn("dial clockwise")