
    # Steps:
    #  1. Line up the gripper as viewed from in front
    #  2. Push down on the handle from the top
    # Line up the robot's gripper as viewed from in front.
    if check("the robot's gripper is not forward aligned with handle"):
        robot.move_gripper("almost forward aligned with handle", close_gripper=True)
    # Once the gripper is aligned, just push the handle down.
    if check("the robot's gripper is forward aligned with handle"):
        robot.move_gripper("vertically aligned with handle")

# peg-insert-side-offset: grab the peg and insert it into the hole from the
# side (with a different orientation than peg-insert-side)
def peg_insert_side_offset(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg becomes right of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not right of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("peg is horizontally aligned with hole"):
        robot.move_gripper("above the peg")
    # If the peg is lined up with the hole to the side, insert it.
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.move_gripper("horizontally aligned with hole")

# button-press: push the button down by pushing