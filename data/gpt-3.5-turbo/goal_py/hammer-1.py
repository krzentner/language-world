# Steps:
    #  1. Move the gripper above the hammer and nail
    #  2. Close the gripper around the hammer handle
    #  3. Move the hammer above the nail
    #  4. Swing the hammer down onto the nail
    # First, move the gripper above the hammer/nail so we can pick up the hammer.
    if check("the robot's gripper is not above the hammer and nail"):
        robot.move_gripper("above the hammer and nail")
    # If the gripper isn't around the hammer yet, move the gripper closer and
    # close the gripper to grab the hammer.
    if check("the robot's gripper is above the hammer and nail and the robot's gripper is not around hammer"):
        robot.move_gripper("around the hammer handle", close_gripper=True)
    # Now that the gripper is around the hammer handle, move the hammer above
    # the nail.
    if check("the robot's gripper is around hammer handle and the hammer is not vertically aligned with the nail"):
        robot.move_gripper("vertically aligned with the nail")
    # Finally, swing the hammer down to hit the nail.
    if check("the robot's gripper is around hammer handle and the hammer is vertically aligned with the nail"):
        robot.move_gripper("above the hammer and nail")  # reset hammer position
        robot.move_gripper("around the hammer handle", close_gripper=True)
        robot.move_gripper("vertically aligned with the nail", close_gripper=True)
        robot.move_gripper("above the hammer and nail", close_gripper=True)  # reset hammer position again