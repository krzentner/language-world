if check("the robot's gripper is not holding the stick"):
        robot.hold("the stick")
    if check("the robot's gripper is not aligned with the thermos"):
        robot.move("the gripper to be in front of the thermos")
    if check("the robot's gripper is touching the thermos with the stick"):
        robot.push("the thermos to the goal using the stick")