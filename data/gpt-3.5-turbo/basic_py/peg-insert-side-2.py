if check("the robot's gripper is not near the peg"):
        robot.move("gripper to the peg")
    if check("the robot's gripper is near the peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the peg is not aligned with the hole and the robot's gripper is around the peg"):
        robot.move("peg to the hole")
    if check("the peg is aligned with the hole and the robot's gripper is around the peg"):
        robot.push("peg into the hole")