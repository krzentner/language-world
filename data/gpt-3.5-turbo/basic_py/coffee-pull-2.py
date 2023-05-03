    if check("the robot's gripper is not near the mug handle"):
        robot.grab("mug handle")
    if check("the robot's gripper is vertically aligned with the mug handle and the robot's gripper is not near the goal"):
        robot.pull("mug to the goal")
    if check("the robot's gripper is near the goal and the mug is below the robot's gripper"):
        robot.release("mug at the goal")