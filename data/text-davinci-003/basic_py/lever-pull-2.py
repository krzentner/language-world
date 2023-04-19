
    if check("the robot's gripper is not above the lever"):
        robot.put("gripper above lever")
    if check("the robot's gripper is above the lever and the lever is not forward aligned with the robot's gripper"):
        robot.rotate("lever up")
    if check("the lever is forward aligned with the robot's gripper"):
        robot.pull("lever up")