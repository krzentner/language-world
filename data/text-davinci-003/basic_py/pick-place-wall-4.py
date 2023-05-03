
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is not forward aligned with wall and the robot's gripper is above puck and the robot's gripper is closed"):
        robot.align("gripper in front of wall")
    if check("the robot's gripper is forward aligned with wall"):
        robot.place("puck at goal")