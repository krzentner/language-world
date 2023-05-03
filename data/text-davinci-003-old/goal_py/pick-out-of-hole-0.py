
    # Steps:
    #  1. Put gripper roughly above the peg
    #  2. Drop the gripper arms around the peg
    #  3. Pick up the peg
    #  4. Move the peg to the target location
    # First, put the gripper roughly above the peg.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("above the peg")
    # If the peg becomes left of the robot's gripper, go back to putting the 
    # gripper above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("the peg is not left of the robot's gripper and the peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg")
    # Once the gripper is lined up with the peg from the front, drop the arms
    # around the peg to pick it up.
    if check("the peg is left of the robot's gripper and the robot's gripper is not around peg"):
        robot.move_gripper("around the peg", close_gripper=True)
    # Now that the gripper is around the peg, pick it up.
    if check("the robot's gripper is around peg"):
        robot.move_gripper("above the target location")