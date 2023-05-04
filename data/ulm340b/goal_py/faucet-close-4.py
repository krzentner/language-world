
    # Steps:
    #  1. Grab handle
    #  2. Turn handle
    # If the gripper isn't aligned with the handle from the front, move the
    # gripper to line up with the handle from the front.
    if check("the robot's gripper is not almost vertically aligned with faucet handle"):
        robot.move_gripper("almost vertically aligned with the faucet handle")
    # If the gripper is lined up with the handle from the front, but isn't
    # near the handle, we can probably grab the handle and turn it.
    if check("the robot's gripper is almost vertically aligned with faucet handle"):
        robot.move_gripper("near faucet handle")

# peg-insert-side-long: grab the peg and insert it into the hole from the
# side, with a long peg
def peg_insert_side_long(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
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
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.move_gripper("above the peg")
    # If the peg is lined up with the hole to the side, insert it.
    if check("peg is horizontally aligned with hole"):
        robot.move_gripper