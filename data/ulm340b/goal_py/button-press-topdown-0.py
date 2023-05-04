
    # Steps:
    #  1. Put gripper above button
    #  2. Start pushing button into hole
    #  3. Press button harder into the hole
    # If the button is not left of the robot's gripper, we should move the
    # gripper above the button to start pushing
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("above the button")
    # If the gripper is around the button we can probably press the button
    # harder into the hole.
    if check("the robot's gripper is near the button"):
        robot.move_gripper("above the button", close_gripper=True)

# peg-insert-top: grab the peg and insert it into the hole from above
def peg_insert_top(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg straight down into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("peg is vertically aligned with hole"):
        robot.move_gripper("above the peg")
    # If the peg is lined up with the hole from above, insert it.
    if check("the robot's gripper is forward aligned with the peg"):
        robot.move_gripper("vertically aligned with hole", open_gripper=True)

# door