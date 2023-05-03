
    if check("the robot's gripper is not near the target location and the wall is between the robot's gripper and the target location"):
        robot.grab("wall")
    if check("the wall is held by the robot's gripper and the wall is near the target location"):
        robot.place("wall at target location")
    if check("the wall is at the target location and the robot's gripper is not near reach target"):
        robot.reach("to target location")