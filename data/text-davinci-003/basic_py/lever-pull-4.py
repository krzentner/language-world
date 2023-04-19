
    if check("the robot's gripper is not vertically aligned with the lever"):
        robot.put("gripper above lever")
    if check("the robot's gripper is not near lever"):
        robot.reach("to lever")
    if check("the robot's gripper is near lever and the lever is down"):
        robot.pull("up lever")