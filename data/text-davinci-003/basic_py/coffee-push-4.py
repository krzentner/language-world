
    if check("the robot's gripper is not close to the mug"):
        robot.reach("to mug")
    if check("the robot's gripper is close to the mug and the mug is to the left of the robot's gripper"):
        robot.pull("mug to the right")
    if check("the robot's gripper is close to the mug and the mug is to the right of the robot's gripper"):
        robot.push("mug to the left")
    if check("the robot's gripper is close to the mug and the mug is to the goal"):
        robot.move("mug to the goal")