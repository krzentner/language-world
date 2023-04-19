
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move("gripper above peg")
    if check("the robot's gripper is vertically aligned with peg and the peg is not inside the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is above the peg and the peg is inside the robot's gripper"):
        robot.lift("peg upward")
    if check("the robot's gripper is above the peg and the peg is outside the robot's gripper"):
        robot.place("peg at location")