if check("the robot's gripper is not vertically aligned with button"):
        robot.move("gripper forward to button")
    if check("the robot's gripper is near the wall"):
        robot.lift("gripper above wall")
    if check("the robot's gripper is vertically aligned with button and the wall is between the robot and button"):
        robot.push("down on button")