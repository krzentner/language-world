
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the handle from the top
    #  3. Let up on the handle
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with the handle")
    # Now that the gripper is lined up, just push down on the handle.
    if check("the robot's gripper is vertically aligned with handle"):
        robot.move_gripper("near the handle")
    # After the gripper is near the handle, move it away from the handle to push
    # the handle down.
    if check("the robot's gripper is near handle and the robot's gripper is vertically aligned with handle"):
        robot.move_gripper("near the handle")

# peg-insert-side-v1: grab the peg and insert it into the hole from the side
def peg_insert_side_v1(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the gripper is lined up with the peg, we can try grabbing the peg.
    # The peg is a long object, so check if the gripper is lined up with it from
    # the front instead of around it.
    if check("peg is left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with the peg and the peg is horizontally aligned