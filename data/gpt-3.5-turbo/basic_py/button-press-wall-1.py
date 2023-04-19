if check("the robot's gripper is not in front of the button and there is a wall between the button and gripper"):
        robot.move("gripper to side of button")
    if check("the robot's gripper is in front of the button and there is a wall between the button and gripper"):
        robot.move("gripper above button and wall")
    if check("the robot's gripper is above the button and there is a wall between the button and gripper"):
        robot.push("down on button with force")
    if check("the button has been pressed"):
        return "Button has been successfully pressed."