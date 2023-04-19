if check("the robot's gripper is not vertically aligned with the peg and the peg is in the hole"):
        robot.move("above the peg in the hole")
    if check("the robot's gripper is above the peg in the hole"):
        robot.grab("the peg")
    if check("the robot's gripper is holding the peg"):
        robot.move("the peg to the target location")