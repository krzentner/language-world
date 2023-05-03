if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is not above the wall"):
        robot.lift("gripper above the wall")
    if check("the robot's gripper is above the button"):
        robot.drop("gripper onto button and push down")