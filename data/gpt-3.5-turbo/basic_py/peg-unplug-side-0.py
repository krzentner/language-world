if check("the robot's gripper is not near the peg"):
        robot.move("gripper to the side of the peg")
    if check("the robot's gripper is next to the peg and the robot's gripper is not vertically aligned with the peg"):
        robot.align("gripper vertically with peg")
    if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is holding the peg"):
        robot.pull("peg out of the hole")