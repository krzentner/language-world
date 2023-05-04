
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Wrap the wrench around the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.move_gripper("vertically aligned with the wrench")
    # If the wrench isn't left of the gripper, it is probably lined up above it,
    # so we should try to grab it.
    # Because the wrench is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("the wrench is forward aligned with the robot's gripper and the wrench is not left of the robot's gripper"):
        robot.move_gripper("left of the wrench", close_gripper=True)
    # Once the wrench is lined up above the robot's gripper, try to grab it by
    # moving the gripper around it.
    # Because the wrench is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("the robot's gripper is forward aligned with the wrench"):
        robot.move_gripper("above the wrench")
    # If the wrench is above the gripper, we should be able to grab it by
    # closing the gripper.
    # Because the wrench is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("the robot's gripper is forward aligned with the wrench"):
        robot.move_gripper("near the wrench")
    # If the robot's gripper is below the wrench, maybe we can grab it by
    # closing the gripper.
    # Because the wrench is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("the robot's gripper is forward aligned with the wrench"):
        robot.move_gripper("below the wrench")
    # If the wrench is below the robot's gripper, we've probably grabbed it, so
    # try to wrap it around the peg by moving the gripper around the peg.
    # Because the wrench