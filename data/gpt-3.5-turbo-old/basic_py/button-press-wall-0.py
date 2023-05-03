if check("the robot's gripper is not forward aligned with the button and the wall is in the way"):
        robot.move("gripper to right of button")
    if check("the robot's gripper is aligned with the button and the wall is in the way"):
        robot.push("button from front with wall in the way")