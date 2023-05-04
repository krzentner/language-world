
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Move the robot's gripper towards the button
    # Line up the robot's gripper from the front.
    if check("the robot's gripper is not horizontally aligned with the button"):
        robot.move_gripper("horizontally aligned with the button")
    # Now that the gripper is lined up, just push towards the button.
    if check("the robot's gripper is horizontally aligned with the button"):
        robot.move_gripper("near the button")

# peg-insert-topdown: insert the peg into the hole from above
def peg_insert_topdown(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg down into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg becomes right of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not right of the robot's gripper and peg is not horizontally aligned with the robot's gripper"):
        robot.move_gripper("horizontally aligned with the peg", close_gripper=True)
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("peg is horizontally aligned with the hole"):
        robot.move_gripper("above the peg")
    # If the peg is lined up with the hole from above, insert it.
    if check("the robot's gripper is horizontally aligned with the peg and the peg is not vertically aligned with hole"):
        robot.move_gripper("vertically aligned with hole")

# peg-unstack-side: grab the top peg and move it to the side
def peg_unstack_side(robot):
    #