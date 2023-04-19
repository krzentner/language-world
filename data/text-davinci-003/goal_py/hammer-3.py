
    # Steps:
    #  1. Put gripper above the head of the nail
    #  2. Push the hammer against the nail, grooving the nails head
    #  3. Hit the nail with the hammer
    # To hit the nail with the hammer, the robot needs to move its gripper fairly
    # accurately above the nail head.
    if check("the robot's gripper is not above the head of the nail"):
        robot.move_gripper("above the head of the nail")
    # Then the robot should be able to push the hammer against the nail,
    # grooving the nail head.
    if check("the robot's gripper is above the head of the nail"):
        robot.move_gripper("near the head of the nail")
    # Finally, we can hit the nail with the hammer.
    if check("the robot's gripper is near the head of the nail"):
        robot.move_gripper("above the head of the nail")