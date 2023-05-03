
    # Steps:
    #  1. Put gripper left of nail
    #  2. Lower gripper down to hammer
    #  3. Pick up the hammer
    #  4. Put the hammer over the nail
    #  5. Lower the hammer onto the nail
    #  6. Hit the nail with the hammer
    # First, move the robot's gripper to the left of the nail.
    # We don't need to line it up with the nail, just make sure it's to the left.
    if check("the robot's gripper is not left of nail"):
        robot.move_gripper("left of nail")
    # If the hammer is below the robot's gripper, lower the gripper to catch the
    # hammer.
    # We don't need to be close to the hammer, just lower the gripper a bit.
    if check("the robot's gripper is not below hammer"):
        robot.move_gripper("below hammer")
    # If the hammer is under the gripper and the gripper is open, we can try to
    # grab the hammer.
    if check("the robot's gripper is below hammer and the robot's gripper is closed"):
        robot.move_gripper("near the nail")
    # If the hammer is above the nail, and the gripper is near it, lower the
    # hammer onto the nail to hit it.
    if check("the robot's gripper is near the nail and the hammer is above nail"):
        robot.move_gripper("over the nail")
    # Finally, hit the nail with the hammer.
    if check("the robot's gripper is over the nail and the hammer is below nail"):
        robot.move_gripper("towards the nail")