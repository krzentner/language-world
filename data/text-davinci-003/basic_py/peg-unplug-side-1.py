
    if check("the robot's gripper is not near the peg"):
        robot.reach("gripper close to peg")
    if check("the robot's gripper is near the peg and peg is not left of the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is left of the peg and peg is not backwards aligned with robot's gripper"):
        robot.align("peg to robot")
    if check("the robot's gripper is backwards aligned with the peg"):
        robot.pull("peg away from hole")