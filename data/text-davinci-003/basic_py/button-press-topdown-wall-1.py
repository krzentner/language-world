
    if check("the robot's gripper is not vertically aligned with button and there is a short wall in the way"):
        robot.put("gripper above wall")
    if check("the robot's gripper is forward aligned with button"):
        robot.push("down on button")