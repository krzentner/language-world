
    if check("the robot's gripper is not near the puck"):
        robot.reach("puck")
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is around the puck and the robot's gripper is closed"):
        robot.grab("puck")
    if check("the robot's gripper is near the target location"):
        robot.place("puck at target")