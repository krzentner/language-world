# peg-unplug-side: grab the peg and pull it out from the side
def peg_unplug_side(robot):
    # Steps:
    #  1. Put gripper around the peg
    #  2. Pull the peg out while moving gripper to the left
    # First, put the gripper around the peg.
    if check("the robot's gripper is not around the peg and the robot's gripper is open"):
        robot.move_gripper("near the peg", close_gripper=True)
    # Once the gripper is around the peg, we can start pulling it out
    # by moving the gripper to the left.
    if check("the robot's gripper is around the peg and the robot's gripper is not left of the peg"):
        robot.move_gripper("left of the peg")