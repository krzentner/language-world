
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # We can go a little farther back than "above" to avoid running into the
    # short wall.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")

# peg-insert-topdown: grab the peg from above and insert it into the hole from above
def peg_insert_topdown(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg down into the hole
    # First, put the gripper above the peg.
    # Because the peg is a long object, we should check if the gripper is lined
    # up with it from the front instead of around it.
    if check("peg is not horizontally aligned with hole and the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    if check("peg is not horizontally aligned with hole and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # As long the gripper is still around the peg and the peg isn't lined up
    # with the hole, line up the peg with the hole.
    if check("peg is horizontally aligned with hole"):
        robot.move_gripper("above the peg", close_gripper=True)
    # If the peg is aligned with the hole from the top, insert it.
    if check("the robot's gripper is forward aligned with the peg and peg is not horizontally aligned with hole