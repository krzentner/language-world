if check("the robot's gripper is not above the ball and the robot's gripper is not vertically aligned with the ball"):
        robot.put("the gripper above the ball")
    if check("the robot's gripper is vertically aligned with the ball and the robot's gripper is not near the ball"):
        robot.push("the gripper into the ball")
    if check("the robot's gripper is near the ball and the ball is below the robot's gripper"):
        robot.slide("the ball into the goal")