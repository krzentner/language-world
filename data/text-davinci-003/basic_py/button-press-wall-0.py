
    if check("the robot's gripper is not behind the short wall"):
        robot.put("gripper to the left of the wall")
    if check("the robot's gripper is behind the short wall and the wall is not vertically aligned with the button"):
        robot.snap("wall in place against button")
    if check("the robot's gripper is behind the short wall and the wall is in place"):
        robot.push("wall forward to press button")