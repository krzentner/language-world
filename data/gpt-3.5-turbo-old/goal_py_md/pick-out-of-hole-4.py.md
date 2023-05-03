# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
# def pick_out_of_hole(robot):

# Steps:
#  1. Put gripper near the hole
#  2. Move the gripper down over the hole
#  3. Close the gripper around the peg
#  4. Lift the gripper out of the hole
#  5. Move the gripper to the target location

if check("the robot's gripper is not above the hole"):
    robot.move_gripper("near the hole")

if check("the robot's gripper is above the hole and the gripper is not around the peg"):
    robot.move_gripper("over the peg", close_gripper=True)

if check("the robot's gripper is around the peg"):
    robot.move_gripper("above the hole")

if check("the robot's gripper is above the hole and the gripper is open"):
    robot.move_gripper("above the target location", close_gripper=True)

# Done!