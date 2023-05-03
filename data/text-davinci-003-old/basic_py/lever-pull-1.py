
    if check("the robot's gripper is not vertically aligned with lever"):
        robot.put("gripper above lever")
    if check("the robot's gripper is vertically aligned with lever"):
        robot.pull("lever up")
        robot.rotate("lever up")