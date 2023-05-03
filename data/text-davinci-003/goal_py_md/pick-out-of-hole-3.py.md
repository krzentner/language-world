

# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above hole
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Lift bag out of hole
    #  5. Move peg to goal
    # First, move the gripper above the hole.
    if check("the robot's gripper is not vertically aligned with the hole"):
        robot.move_gripper("vertically aligned with the hole")
    # Now we need to grab the peg, so let's drop the gripper around it.
    if check("the robot's gripper is not around the peg"):
        robot.move_gripper("near the peg", close_gripper=True)
    # Once the gripper is around the peg, close it to make sure the peg is securely
    # in the gripper.
    # If the gripper is near the peg and closed, we should be able to lift it out 
    # of the hole.
    if check("the robot's gripper is around the peg and the robot's gripper is closed"):
        robot.move_gripper("above the hole")
    # Now that the peg is free, we can move it to the target location.
    if check("the robot's gripper is above the hole"):
        robot.move_gripper("near the target location")