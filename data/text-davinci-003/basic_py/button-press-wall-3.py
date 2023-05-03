
    if check("the robot's gripper is not above the wall and the robot's gripper is not horizontally aligned with the wall"):
        robot.put("gripper above wall")
    if check("the robot's gripper is above the wall"):
        robot.align("gripper to wall")
    if check("the robot's gripper is horizontally aligned with the wall and the wall is not horizontally aligned with the button"):
        robot.push("wall towards button")
    if check("the wall is horizontally aligned with the button"):
        robot.push("down on button")