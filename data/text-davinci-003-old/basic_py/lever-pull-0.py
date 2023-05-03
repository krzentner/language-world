
    if check("the robot's gripper is not above the lever"):
        robot.put("gripper above lever")
    if check("the robot's gripper is above the lever and the lever is not rotated up"):
        robot.pull("lever up")