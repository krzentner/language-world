
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Close the drawer handle
    # First, put the gripper mostly above the drawer handle.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle", close_gripper=True)
    # Now that the gripper is lined up, we can just push the drawer handle in to
    # close the drawer.
    if check("the robot's gripper is vertically aligned with drawer handle"):
        robot.move_gripper("in front of the drawer handle")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Close the door handle
    # First, put the gripper mostly above the door handle.
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.move_gripper("vertically aligned with the door handle", close_gripper=True)
    # Now that the gripper is lined up, we can just push the door handle in to
    # close the door.
    if check("the robot's gripper is vertically aligned with door handle"):
        robot.move_gripper("in front of the door handle")

# hook-sweep-into-hole: put the peg in the hole using the hook
def hook_sweep_into_hole(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Pick up the peg
    #  3. Put the peg in front of the hole
    #  4. Push the peg into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg", close_gripper=True)
    # Now that the robot's gripper is above the peg, we can grab the peg.
    if check("the robot's gripper is vertically aligned with the peg"):
        robot.move_gripper("above the peg")
    # When the gripper is above the peg, we can just bring it towards the hole.
    # Because the