if check("the robot's gripper is not near the peg"):
        robot.move("gripper to peg")
    if check("the robot's gripper is near the peg and the robot's gripper is not around the peg"):
        robot.grab("peg")
    if check("the robot's gripper is around the peg"):
        robot.move("gripper to hole")
    if check("the robot's gripper arm is aligned with the hole"):
        robot.move("gripper closer to the hole")
    if check("the peg is inserted into the hole"):
        robot.release("peg")