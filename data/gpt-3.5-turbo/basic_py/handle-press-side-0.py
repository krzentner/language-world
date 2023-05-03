if check("the robot's gripper is not horizontally aligned with the handle"):
        robot.move("gripper to the side of handle")
    if check("the robot's gripper is near the handle"):
        robot.push("down on handle")