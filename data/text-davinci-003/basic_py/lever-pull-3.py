
    if check("the robot's gripper is not forward aligned with the lever"):
        robot.put("gripper in front of lever")
    if check("the robot's gripper is forward aligned with the lever and the lever is below the grip"):
        robot.grab("lever")
    if check("gripper is around lever"):
        robot.pull("lever up")