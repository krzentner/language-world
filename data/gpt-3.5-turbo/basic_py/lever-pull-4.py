if check("the robot's gripper is not near the lever"):
        robot.move("gripper to right of lever")
    if check("the robot's gripper is below the lever"):
        robot.move("gripper below lever")
    if check("the robot's gripper is below and around the lever and the robot's gripper is not gripping the lever"):
        robot.grab("lever")
    if check("the robot's gripper is around the lever and the lever is pointing down"):
        robot.rotate("the lever up")