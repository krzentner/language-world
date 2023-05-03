if check("the robot's gripper is not vertically aligned with the lever and the robot's gripper is not near the lever"):
        robot.move("gripper to lever")
    if check("the robot's gripper is near the lever and the robot's gripper is not around the lever"):
        robot.grab("lever")
    if check("the robot's gripper is around the lever and the lever is not up"):
        robot.rotate("lever up")