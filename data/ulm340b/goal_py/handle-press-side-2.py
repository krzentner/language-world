
    # Steps:
    #  1. Line up the gripper with the handle as seen from in front
    #  2. Push the handle down
    # First, put the gripper to the side of the handle.
    if check("the robot's gripper is not horizontally aligned with handle"):
        robot.move_gripper("near the handle")
    # As long as we are to the side of the handle, push down on it to try to
    # push it down.
    if check("the robot's gripper is not horizontally aligned with handle"):
        robot.move_gripper("near the handle")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper right of the door handle
    #  2. Start pushing against the door handle to close the door
    #  3. Push the door closed harder
    # If the the door handle is right of the robot's gripper, we should move the
    # gripper near the door handle to start pushing
    if check("the robot's gripper is in front of the door handle"):
        robot.move_gripper("right of the door handle")
    # If the robot's gripper is near the door handle we can probably push the
    # door closed now by moving the gripper right.
    if check("the door handle is right of the robot's gripper and the robot's gripper is not near the door handle"):
        robot.move_gripper("almost vertically aligned with the door handle")
    # If the robot's gripper is starting to be in front of the door handle, push
    # harder.
    if check("the robot's gripper is near the door handle"):
        robot.move_gripper("forward aligned with the door handle")

# peg-insert-topdown: grab the peg and insert it into the hole from above
def peg_insert_topdown(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Drop the peg into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned