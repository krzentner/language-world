

# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper horizontally aligned with peg
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Move peg to target location 
    # First, put the robot's gripper horizontally aligned with the peg, so that 
    # we can grab it from the side.
    if check("the robot's gripper is not almost horizontally aligned with peg"):
        robot.move_gripper("almost horizontally aligned with the peg", close_gripper=True)
    # Once the gripper is near the peg, we should be able to grab it with the 
    # robot's finger and slot it into the peg.
    if check("the robot's gripper is horizontally aligned with peg and the robot's gripper is not around peg"):
        robot.move_gripper("around the peg", close_gripper=True)
    # If the gripper is around the peg, we can move the peg to the target 
    # location.
    if check("the robot's gripper is around peg"):
        robot.move_gripper("near the target location")