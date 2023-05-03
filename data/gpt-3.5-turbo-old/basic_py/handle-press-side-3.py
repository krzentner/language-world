    if check("the robot's gripper is not near the handle"):
        robot.move("gripper to side of handle")
    if check("the robot's gripper is horizontally aligned with the handle"):
        robot.push("down on handle from the side")