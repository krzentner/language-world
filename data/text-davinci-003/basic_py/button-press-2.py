
    if check("the robot's gripper is not sideways aligned with button and the robot's gripper is not horizontally aligned with the button"):
        robot.align("gripper to button")
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("on button")