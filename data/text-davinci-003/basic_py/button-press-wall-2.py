
    if check("the robot's gripper is not forward aligned with the button and the robot's gripper is not near the wall"):
        robot.move("gripper near the wall near the button")
    if check("the robot's gripper is near the wall near the button"):
        robot.push("gripper forward to the button")
    if check("the robot's gripper is not forward aligned with the button and the robot's gripper is near the wall"):
        robot.push("gripper forward to the button")