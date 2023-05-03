
    # Steps:
    #  1. Put gripper above plate
    #  2. Grab plate with gripper
    #  3. Line up plate with back wall of target
    #  4. Slide plate from side to side back into target
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # As long as the plate isn't left of the gripper, we should be able to grab
    # the plate by moving the gripper down around the plate.
    # Note that we're checking to see if the plate is forward aligned with the
    # gripper and not around the gripper, since the plate is rather large and
    # won't fit all the way around the gripper.
    if check("the plate is not left of the robot's gripper and the plate is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the plate", close_gripper=True)
    # If the plate is not aligned with the back wall of the target, align it.
    if check("the plate is left aligned with back side target wall"):
        robot.move_gripper("above the plate")
    # If the plate is aligned with the back wall of the target, we can slide it
    # back into the target.
    if check("the plate is left aligned with the back side target wall and the robot's gripper is forward aligned with the plate"):
        robot.move_gripper("left aligned with back side target wall")