
    if check("the robot's gripper is below the lever and the lever is right of the robot's gripper"):
        robot.move("gripper to left of lever")
    if check("the robot's gripper is near the lever"):
        robot.pull("lever up")