if check("the robot's gripper is not around the lever and the robot's gripper is open"):
        robot.grab("the lever")
    if check("the robot's gripper is around the lever and the lever is not in upward position"):
        robot.rotate("the lever up")