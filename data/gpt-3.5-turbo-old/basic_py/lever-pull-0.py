if check("the robot's gripper is not around the lever and the robot's gripper is open"):
        robot.grab("lever")
    if check("the robot's gripper is around the lever"):
        robot.pull("lever up")