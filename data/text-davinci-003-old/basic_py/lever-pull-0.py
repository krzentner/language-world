
    if check("the robot's gripper is not vertically aligned with the lever"):
        robot.put("gripper above lever")
    if check("the robot's gripper is vertically aligned with the lever and the lever is not above the robot's gripper"):
        robot.grab("lever")
    if check("the lever is above the robot's gripper"):
        robot.pull("lever up")