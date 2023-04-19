

If check("the robot's gripper is not above the peg"):
    robot.grab("peg")
if check("the peg is not below the robot's gripper and the peg is not forward aligned with the robot's gripper"):
    robot.align("peg to robot's gripper")
if check("the peg is below the robot's gripper and the robot's gripper is forward aligned with the peg"):
    robot.pull("peg out of hole")