
    # Steps:
    #  1. Grab the peg with the gripper
    #  2. Unplug peg by sliding sideways
    # First, grab the peg with the gripper.
    if check("the robot's gripper is not around the peg"):
        robot.move_gripper("around the peg")
    # Once we've got the peg in the gripper, slide the peg sideways to unplug it.
    # Move the gripper to the side until the peg is just barely out of the hole.
    if check("the peg is free from the hole"):
        robot.move_gripper("near the peg")