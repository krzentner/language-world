

# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper in front of peg
    #  2. Move gripper around peg to pick up peg
    #  3. Close gripper around peg
    #  4. Move gripper over hole in the target location
    #  5. Insert peg into the hole from the side
    # First, put the gripper in front of the peg, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not in front of the peg"):
        robot.move_gripper("in front of the peg")
    # If the gripper is in front of the peg, but not around it, move the
    # gripper around it to pick it up.
    if check("the robot's gripper is in front of the peg and the robot's gripper is not around peg"):
        robot.move_gripper("around the peg", close_gripper=True)
    # If the gripper is around the peg and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is around peg and the robot's gripper is closed"):
        robot.move_gripper("near the target location")
    # If the gripper is in front of the hole and the peg is in the gripper,
    # slide the peg into the hole from the side.
    if check("the robot's gripper is in front of the hole and the peg is in the robot's gripper"):
        robot.move_gripper("on the other side of the hole")