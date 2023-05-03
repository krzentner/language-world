
    if check("the robot's gripper is not next to the lever"):
        robot.put("gripper next to lever")
    if check("the robot's gripper is next to the lever"):
        robot.pull("lever up")