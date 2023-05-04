
    # Steps:
    #  1. Put gripper above box lid
    #  2. Grab box lid
    #  3. Put lid on box
    # If the box lid is below the gripper, put the gripper above the box lid.
    if check("the robot's gripper is not vertically aligned with the box lid"):
        robot.move_gripper("vertically aligned with the box lid")
    # If the gripper is above the box lid, try grabbing the box lid by closing
    # the gripper.
    if check("the robot's gripper is vertically aligned with the box lid"):
        robot.move_gripper("almost vertically aligned with the box lid", close_gripper=True)
    # If the robot's gripper is around the box lid, place it on the box.
    # Because the box lid is a long object, check if the gripper is lined up
    # with it from the front instead of around it.
    if check("the robot's gripper is vertically aligned with the box lid and the robot's gripper is not around the box lid"):
        robot.move_gripper("above the box")

# peg-insert-side-hole: pick up the peg and insert it into the side hole
def peg_insert_side_hole(robot):
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
