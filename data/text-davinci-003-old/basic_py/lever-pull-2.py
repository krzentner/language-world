
    if check("the robot's gripper is not vertically aligned with lever"):
        robot.put("gripper above lever")
    if check("the robot's gripper is vertically aligned with lever and lever is not near the robot's gripper"):
        robot.grab("lever")
    if check("lever is near the robot's gripper"):
        robot.rotate("lever upwards")