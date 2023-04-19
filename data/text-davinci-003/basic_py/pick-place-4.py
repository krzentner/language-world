
    if check("the robot's gripper is not above the puck"):
        robot.reach("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.grab("puck")
    if check("the robot's gripper is around the puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is around the puck and the robot's gripper is closed"):
        robot.place("puck at goal")