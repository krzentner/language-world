if check("the robot's gripper is not near peg"):
        robot.move("gripper towards peg")
    if check("the robot's gripper is near peg and the robot's gripper is not around peg"):
        robot.grab("peg")
    if check("the robot's gripper is around peg and the peg is not near the hole"):
        robot.move("peg to the side of the hole")
    if check("the peg is near the hole and the robot's gripper is around peg"):
        robot.rotate("peg to align with hole")
    if check("the peg is aligned with the hole"):
        robot.push("peg into the hole")
    if check("the peg is inside the hole"):
        robot.release("peg")