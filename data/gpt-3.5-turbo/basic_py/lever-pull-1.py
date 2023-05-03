if check("the robot's gripper is not near the lever"):
        robot.move("gripper to left of lever")
    if check("the robot's gripper is near the lever"):
        robot.push("lever up")