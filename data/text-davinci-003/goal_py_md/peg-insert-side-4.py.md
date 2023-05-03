

# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper in front of peg
    #  2. Drop gripper onto peg
    #  3. Push peg into hole
    # First, line up the robot's gripper with the peg, so that it can grab the
    # peg.
    if check("the robot's gripper is not in front of peg"):
        robot.move_gripper("in front of the peg")
    # Then, once the gripper is in front of the peg, we can drop the gripper
    # onto the peg.
    if check("the robot's gripper is in front of peg"):
        robot.move_gripper("above the peg", close_gripper=True)
    # Once the gripper is above the peg and close, it should be able to hold the
    # peg securely. Now we just need to push the peg into the hole.
    if check("the peg is above the robot's gripper and the robot's gripper is closed"):
        robot.move_gripper("against the side of the hole")