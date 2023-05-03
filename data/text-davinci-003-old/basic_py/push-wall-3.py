
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.grab("puck")
    if check("the robot's gripper is above puck and the robot's gripper is not above wall"):
        robot.upper("gripper above wall")
    if check("the robot's gripper is above wall and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")