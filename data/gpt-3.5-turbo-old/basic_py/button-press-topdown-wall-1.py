If check("robot's gripper is not vertically aligned with button"):
        robot.move("above the button")
    if check("there is a wall between the robot's gripper and the button"):
        robot.move("to a position where the gripper is not obstructed by the wall")
    if check("the robot's gripper is vertically aligned with the button and not obstructed by the wall"):
        robot.push("down on button")