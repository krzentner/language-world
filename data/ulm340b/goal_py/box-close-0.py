
    # Steps:
    #  1. Put gripper above box lid
    #  2. Drop gripper around box lid
    #  3. Close gripper around box lid
    #  4. Move box lid to be above the box
    #  5. Release box lid
    # First, put the gripper roughly above the box lid, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the box lid"):
        robot.move_gripper("above the box lid")
    # If the gripper isn't around the box lid, put it around the box lid.
    if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
        robot.move_gripper("near the box lid", close_gripper=True)
    # If the gripper is around the box lid and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is around the box lid"):
        robot.move_gripper("above the box lid")

# drawer-insert: grab the drawer and insert it into the slot
def drawer_insert(robot):
    # Steps:
    #  1. Put gripper above the drawer handle
    #  2. Drop gripper around the drawer handle
    #  3. Close gripper around the drawer handle
    #  4. Push the drawer into the hole
    # Because the drawer is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with the drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")
    # If the gripper isn't around the drawer handle, put it around the drawer
    # handle.
    # Because the drawer is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("the robot's gripper is not forward aligned with the drawer handle and the robot's gripper is open"):
        robot.move_gripper("forward aligned with the drawer handle", close_gripper=True)