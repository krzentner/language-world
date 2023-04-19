
    if check("the robot's gripper is not vertically aligned with the lever"):
        robot.put("gripper above lever")
    if check("the robot's gripper is vertically aligned with the lever and the robot's gripper is not around the lever"):
        robot.grab("lever")
    if check("the robot's gripper is around the lever"):
        robot.pull("lever up")