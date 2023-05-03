
    # Steps:
    #  1. Put gripper above the dial
    #  2. Grab the dial
    #  3. Turn the dial
    # First, put the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.move_gripper("vertically aligned with the dial", close_gripper=True)
    # Once the gripper is lined up, we can grab the dial by closing the
    # gripper.
    if check("the robot's gripper is vertically aligned with the dial and the robot's gripper is not near the dial"):
        robot.move_gripper("around the dial")
    # Now that the gripper is near the dial, we can turn it the right direction.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("above the dial")

# peg-remove-side: remove the peg from the side
def peg_remove_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Pull the peg out from the side
    # The robot can grab the peg by moving the gripper above the peg and
    # closing the gripper.
    if check("the robot's gripper is not above the peg and the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg", close_gripper=True)
    # Once the gripper is near the peg and closed, it should be holding the peg.
    # We can then pull the peg out by moving the gripper side ways.
    if check("the robot's gripper is near the peg and the robot's gripper is closed"):
        robot.move_gripper("horizontally aligned with the peg")

# peg-remove-front-one-hand: remove the peg by grabbing it from the front
def peg_remove_front_one_hand(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Pull the peg out from the side
    # The robot can grab the peg by moving the gripper above the peg.
    if check("the robot's gripper is not above the peg and the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg", close_gripper=True)
    # If the