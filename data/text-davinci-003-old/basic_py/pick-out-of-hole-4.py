
    if check("the robot's gripper is not inclined at the peg"):
        robot.put("gripper above the peg")
    if check("gripper is inclined at the peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    if check("gripper is almost closed and the peg is stuck in the hole"):
        robot.rotate("gripper in a circular motion")
    if check("gripper is closed and the peg is no longer stuck in the hole"):
        robot.pick("peg out of hole")
    if check("peg is in the robot's grip and the robot's gripper is above the goal"):
        robot.place("peg at goal")