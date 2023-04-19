
    # Steps:
    #  1. Put gripper near a hammer
    #  2. Grab the hammer with the gripper
    #  3. Put the gripper near the nail
    #  4. Swing the hammer down to drive the nail
    # First, put the gripper near the hammer.
    if check("the robot's gripper is not near hammer"):
        robot.move_gripper("near the hammer")
    # Once the gripper is near the hammer, grab it.
    if check("the robot's gripper is near hammer and the gripper is not closed"):
        robot.move_gripper("near the hammer", close_gripper=True)
    # Now that the hammer is in the robot's gripper, move the gripper
    # towards the nail.
    if check("the robot's gripper is not near the nail"):
        robot.move_gripper("near the nail")
    # Once the gripper is close to the nail, swing the hammer down to drive it.
    if check("the robot's gripper is near the nail"):
        robot.move_gripper("below the nail")