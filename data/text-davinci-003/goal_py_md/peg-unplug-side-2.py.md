

# peg-unplug-side: grab the peg and pull the it out from the side
def peg_unplug_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Pull the peg sideways out of the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the gripper isn't closed, grab it by closing the gripper.
    if check("the robot's gripper is open"):
        robot.move_gripper("above the peg")
    # If the gripper is closed, slide the peg horizontally so we can pull it out.
    if check("the robot's gripper is closed"):
        robot.move_gripper("near the hole")
    # Once the peg is near the hole, we can pull the peg out by moving it
    # horizontally.
    if check("the robot's gripper is near the hole"):
        robot.move_gripper("horizontally aligned with the hole")