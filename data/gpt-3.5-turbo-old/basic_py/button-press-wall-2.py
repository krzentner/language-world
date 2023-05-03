if check("the robot's gripper is not horizontally aligned with the button and the wall"):
        robot.adjust("gripper to align with button and the wall")
    if check("the robot's gripper is aligned with the button and the wall"):
        robot.push("button down")