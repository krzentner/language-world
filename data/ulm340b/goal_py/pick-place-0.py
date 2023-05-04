
    # Steps:
    #  1. Put gripper above the puck
    #  2. Grab the puck with the gripper
    #  3. Move gripper to target location
    #  4. Release the puck at the target location
    # We need to put the gripper above the puck before we can grab it, because
    # of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # Once the gripper is lined up above the puck, we should be able to grab the
    # puck by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not around the puck"):
        robot.move_gripper("around the puck", open_gripper=True)
    # Once the gripper is around the puck, we can just pick it up.
    # Keep closing the gripper as we move it to make sure we don't drop it.
    if check("the robot's gripper is around the puck"):
        robot.move_gripper("vertically aligned with the target location", close_gripper=True)
    # Once we're above the target location, open the gripper to drop it.
    if check("the robot's gripper is vertically aligned with the target location"):
        robot.move_gripper("vertically aligned with the target location", open_gripper=True)

# peg-unstack-side: slide the top peg to the side, then remove it
def peg_unstack_side(robot):
    # Steps:
    #  1. Move gripper to side of the top peg
    #  2. Push the top peg sideways to the edge of the table
    #  3. Grab the top peg and lift it up
    #  4. Put the top peg away
    # If the robot's gripper is not in front of the top peg, we should move it
    # there.
    if check("the robot's gripper is not forward aligned with the top peg"):
        robot.move_gripper("forward aligned with the top peg")
    # Once the gripper is in front of the top peg, we can probably push it off
    # the