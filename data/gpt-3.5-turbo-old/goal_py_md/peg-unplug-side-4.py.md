# peg-unplug-side: pull the peg out from the side
# def peg_unplug_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the gripper up with the peg and pull it out
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # If the gripper is around the peg, pull the peg out.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("horizontally aligned with the peg", close_gripper=True)
        robot.move_gripper("vertically aligned with the peg", close_gripper=False)