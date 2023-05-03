if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is not above the wall"):
        robot.lift("gripper above wall")
    if check("the robot's gripper is above the button"):
        robot.push("down on button while avoiding wall")