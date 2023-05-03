
    if check("the robot's gripper is not near the cube"):
        robot.move("the gripper near the cube")
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.close("the gripper around the cube")
    if check("the robot's gripper is around the cube"):
        robot.sweep("the cube to the goal")