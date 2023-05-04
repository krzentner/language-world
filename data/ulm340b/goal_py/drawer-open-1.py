
    # Steps:
    #  1. Put gripper left of the drawer handle
    #  2. Start pulling against the drawer handle to open the drawer
    #  3. Pull the drawer open harder
    # If the the drawer handle is right of the robot's gripper, we should move
    # the gripper near the drawer handle to start pulling
    if check("the robot's gripper is in front of the drawer handle"):
        robot.move_gripper("right of the drawer handle")
    # If the robot's gripper is near the drawer handle we can probably slide the
    # drawer open now by moving the gripper left.
    if check("the drawer handle is right of the robot's gripper and the robot's gripper is not near the drawer handle"):
        robot.move_gripper("almost vertically aligned with the drawer handle")
    # If the robot's gripper is starting to be in front of the drawer handle,
    # pull harder.
    if check("the robot's gripper is near the drawer handle"):
        robot.move_gripper("forward aligned with the drawer handle")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Push closed the door
    # First, put the gripper above door handle.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.move_gripper("almost vertically aligned with the door handle", close_gripper=True)
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.move_gripper("around the door handle")

# peg-insert-sideway: grab the peg and insert it into the hole from above
def peg_insert_sideway(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Push the peg into the hole
    # First, put the gripper above the peg