# hammer: hit the nail with the hammer
# def hammer(robot):
    # Steps:
    #  1. Put gripper above the hammer
    #  2. Grab the hammer with the gripper
    #  3. Line up hammer with nail
    #  4. Use hammer to hit nail
    # First, put the gripper above the hammer.
    if check("the robot's gripper is not vertically aligned with the hammer"):
        robot.move_gripper("vertically aligned with the hammer")
    # If the hammer isn't grasped by the gripper, put the gripper around it and grab it.
    if check("the robot's gripper is not around the hammer and the robot's gripper is open"):
        robot.move_gripper("near the hammer", close_gripper=True)
    # Once the gripper has the hammer, line it up with the nail.
    if check("the hammer is not near the nail"):
        robot.move_gripper("above the nail")
    # Finally, use the hammer to hit the nail.
    if check("the hammer is near the nail"):
        robot.hit_with_hammer()