
    if check("the peg is not in the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is not in line with the hole"):
        robot.move("gripper to the side of the hole")
    if check("the robot's gripper is in line with the hole"):
        robot.push("peg into the hole")