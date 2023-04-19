
    if check("the robot's gripper is not near the plate and the plate is back of the target"):
        robot.move("gripper near plate")
    if check("the robot's gripper is near plate and plate is not horizontally aligned with target"):
        robot.slide("plate to target")
    if check("the robot's gripper is near plate and the plate is not exactly at target"):
        robot.push("plate slightly into target")