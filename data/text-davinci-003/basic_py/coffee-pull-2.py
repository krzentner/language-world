
    if check("the robot's gripper is not above the mug"):
        robot.put("gripper above mug")
    if check("the robot's gripper is open and the robot's gripper is not around mug"):
        robot.grab("mug")
    if check("the robot's gripper is closed and the mug is not near the target"):
        robot.pull("mug to goal")