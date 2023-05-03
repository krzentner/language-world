if check("the robot's gripper is not in front of the button"):
        robot.move("gripper to front of button")
    if check("the robot's gripper is in front of the button and there is a short wall in between the robot and button"):
        robot.lift("gripper over the wall")
    if check("the robot's gripper is over the wall and in front of the button"):
        robot.push("down on button")