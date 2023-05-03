if check("the robot's gripper is not aligned with the peg and the robot's gripper is not open"):
        robot.open("gripper")
    if check("the robot's gripper is not aligned with the peg and the robot's gripper is open"):
        robot.move("gripper to the side of the peg")
    if check("the robot's gripper is aligned with the peg and the robot's gripper is not closed"):
        robot.grab("peg")
    if check("the robot's gripper is aligned with the hole and the peg is not inside the hole"):
        robot.move("gripper and peg towards the hole")
    if check("the peg is inside the hole and the robot's gripper is close to the hole"):
        robot.push("peg into the hole")
    if check("the peg is completely in the hole and the robot's gripper is close to the hole"):
        robot.release("gripper")