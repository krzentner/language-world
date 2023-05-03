

Solution:

# peg-unplug-side: pull the peg out from the side
# def peg_unplug_side(robot):
    # Steps:
    #  1. Put gripper right of the peg
    #  2. Grab peg with gripper
    #  3. Pull peg out sideways
    # 
    # First, put the gripper near the peg.
    if check("the robot's gripper is not near the peg"):
        robot.move_gripper("near the peg")
    # If the peg is left of the gripper, grab the peg with the gripper.
    if check("the peg is left of the robot's gripper and the robot's gripper is open"):
        robot.move_gripper("around the peg", close_gripper=True)
    # If the peg is right of the gripper, bring the gripper down so that it's
    # almost touching the peg.
    if check("the robot's gripper is almost touching the peg"):
        robot.move_gripper("above the peg")
    # As long as the gripper is still mostly around the peg, pull the peg sideways
    # to slide it out of the hole.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("horizontally aligned with the hole")