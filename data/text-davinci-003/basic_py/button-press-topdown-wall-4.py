
    if check("the robot's gripper is not above the button and the robot's gripper is not vertically aligned with the button"):
        robot.move("gripper to the left of the wall")
        robot.close("gripper around wall")
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is on the left side of the wall"):
        robot.pull("the wall to the right")
    if check("the robot's gripper is vertically aligned with the button and the wall is between the button and the robot's gripper"):
        robot.push("down on button")