

Once you're finished, please report back. I'd also appreciate it if you could describe the general process you followed when writing this code.
"""

# box-close: pick up the box lid and place it on the box
def box_close(robot):
    # Steps:
    #  1. Move gripper above the box lid
    #  2. Lower the gripper on top of the box lid
    #  3. Push down on top of the box lid
    #  4. Move the box lid on top of the box
    #  5. Slide the box lid into place
    # Let's make sure the gripper is on top of the box lid
    if check("the robot's gripper is not above the box lid"):
        robot.move_gripper("above the box lid", close_gripper=True)
    # Lower the gripper onto the box lid
    if check("the robot's gripper is above the box lid"):
        robot.move_gripper("vertically aligned with the box lid")
    # If the gripper is around the box lid, push down on it
    if check("the robot's gripper is above the box lid"):
        robot.move_gripper("almost vertically aligned with the box lid", close_gripper=True)
    # Lower the gripper into place on top of the box
    if check("the robot's gripper is above the box lid"):
        robot.move_gripper("horizontally aligned with the box lid")


# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # First, put the gripper mostly above the door handle.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.move_gripper("almost vertically aligned with the door handle", close_gripper=True)
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.move_gripper("left of the door handle")

# reach: reach to the target location
def reach(robot):
 