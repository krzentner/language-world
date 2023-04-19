

We will use the same process for this task as for the `peg-insert-side` task. 

# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
# def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Pull the peg out of the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # As long the gripper is still mostly around the peg and the peg is not lined
    # up with the hole, line up the peg with the hole.
    if check("the peg is horizontally aligned with the hole and the peg is not left of the robot's gripper"):
        robot.move_gripper("around the peg")
        robot.move_gripper("vertically aligned with the hole")
    # Finally, when the peg is in line with the hole, move it out of the hole by
    # pulling the peg to the left.
    if check("the peg is horizontally aligned with the hole and the peg is left of the robot's gripper"):
        robot.move_gripper("left of the hole")