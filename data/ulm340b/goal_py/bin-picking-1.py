
    # Steps:
    #  1. Put gripper above the cube
    #  2. Drop gripper around the cube
    #  3. Close gripper around the cube
    #  4. Move the cube to the target bin
    # First, put the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with cube"):
        robot.move_gripper("vertically aligned with the cube")
    # If the gripper is above the cube, try moving it around the cube to grab
    # it.
    if check("the robot's gripper is above the cube"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is around the cube, try closing it to grab the cube.
    if check("the robot's gripper is around the cube and the robot's gripper is not near the target bin"):
        robot.move_gripper("horizontally aligned with the target bin")

# drawer-close-topdown: close the drawer from above
def drawer_close_topdown(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Push gripper into the drawer handle
    #  3. Push the drawer closed
    # First, put the gripper above the drawer handle.
    if check("the robot's gripper is not above the drawer handle"):
        robot.move_gripper("above the drawer handle")
    # If the gripper is above the drawer handle, push it down into the drawer
    # handle.
    if check("the robot's gripper is above the drawer handle and the robot's gripper is not near the drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")
    # If the robot's gripper is in front of the drawer handle, we can push the
    # drawer closed.
    if check("the robot's gripper is around the drawer handle"):
        robot.move_gripper("near the drawer handle")

# peg-insert-topdown: insert the peg into the hole from above
def peg_insert_topdown(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
 