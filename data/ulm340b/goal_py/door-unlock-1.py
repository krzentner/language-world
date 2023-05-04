
    # Steps:
    #  1. Put gripper above the door dial
    #  2. Grab the door dial
    #  3. Turn the dial to the left
    # First, put the gripper above the door dial.
    if check("the robot's gripper is not almost vertically aligned with door dial"):
        robot.move_gripper("vertically aligned with the door dial", close_gripper=True)
    # Once the gripper is above the door dial, we can probably grab the dial.
    if check("the robot's gripper is vertically aligned with door dial and the door dial is not left of the robot's gripper"):
        robot.move_gripper("near the door dial")
    # Once we've got the door dial grabbed, we should be able to open it by
    # turning it.
    if check("the robot's gripper is forward aligned with door dial"):
        robot.move_gripper("around the door dial")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Push door closed
    # First, put the gripper above the door handle.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.move_gripper("above the door handle")
    # As long as the gripper is above the door handle, closing it should line
    # the gripper up.
    if check("the robot's gripper is almost vertically aligned with door handle"):
        robot.move_gripper("right of the door handle", close_gripper=True)

# peg-insert-side-long: grab the peg and insert it into the hole from the side
# (long peg)
def peg_insert_side_long(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move