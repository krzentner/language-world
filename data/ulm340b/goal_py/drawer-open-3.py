
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull drawer open
    # If the gripper is not above the drawer handle, put it above the drawer
    # handle.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")
    # As long the gripper is around the drawer handle, we can pull it open.
    if check("the robot's gripper is vertically aligned with drawer handle"):
        robot.move_gripper("left of the drawer handle")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper around the door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it to the door handle.
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # If the door is aligned with the gripper as seen from in front, we can push
    # the door closed.
    if check("the robot's gripper is forward aligned with the door handle"):
        robot.move_gripper("left of the door handle")

def peg_insert_side(robot):
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
        robot.move_gripper("forward