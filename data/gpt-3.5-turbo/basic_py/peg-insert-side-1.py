if check("the robot's gripper is not near the peg and the robot's gripper is not open"):
        robot.release("the peg")
    if check("the robot's gripper is not near the peg and the robot's gripper is open"):
        robot.grasp("the peg")
    if check("the robot's gripper is near the hole and the peg is not inserted"):
        robot.insert("the peg into the hole")
    if check("the robot's gripper is near the hole and the peg is partially inserted"):
        robot.force("the peg until it is fully inserted")