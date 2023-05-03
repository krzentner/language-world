

Steps:
1. Put gripper to the side of the peg
2. Drop gripper around peg
3. Pull peg out of hole
4. Move peg to target location

if check("the robot's gripper is not to the side of the peg"):
    robot.move_gripper("to the side of the peg")

if check("the robot's gripper is not around peg and the robot's gripper is open"):
    robot.move_gripper("near the peg", close_gripper=True)

if check("the robot's gripper is around peg"):
    robot.move_gripper("vertically aligned with the peg and near the hole")

if check("the robot's gripper is around peg and the peg is pulled out of the hole"):
    robot.move_gripper("near the target location")