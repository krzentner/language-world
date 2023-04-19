
    if check("the robot's gripper is not near the stick"):
        robot.grab("stick")
    if check("the robot's gripper is near the stick and the robot's gripper is open"):
        robot.close("gripper around stick")
    if check("the robot's gripper is near the stick and the robot's gripper is closed"):
        robot.pull("stick away from thermos")