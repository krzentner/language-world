
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near the puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is near the puck and the robot's gripper is closed"):
        robot.place("puck at wall")
    if check("the robot's gripper is not around the short wall and the robot's gripper is open"):
        robot.drop("gripper around short wall")
    if check("the robot's gripper is around the wall"):
        robot.push("puck over wall")