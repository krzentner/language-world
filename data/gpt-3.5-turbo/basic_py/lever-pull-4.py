if check("the robot's gripper is not near the lever"):
        robot.approach("the gripper to the lever")
    if check("the robot's gripper is near the lever and the robot's gripper is not around the lever and the robot's gripper is open"):
        robot.pickup("the lever")
    if check("the robot's gripper is around the lever and the lever is not in the up position"):
        robot.move("the lever up")