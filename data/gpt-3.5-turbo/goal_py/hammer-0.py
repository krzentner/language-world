# Steps:
    #  1. Put the gripper above the hammer
    #  2. Drop the gripper around the handle of the hammer
    #  3. Close the gripper around the handle of the hammer
    #  4. Move the hammer above the nail
    #  5. Swing the hammer down onto the nail
    # First, put the gripper roughly above the hammer, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the hammer"):
        robot.move_gripper("above the hammer")
    # If the gripper isn't around the handle of the hammer, put it around the handle.
    if check("the robot's gripper is not around the handle of the hammer and the robot's gripper is open"):
        robot.move_gripper("near the handle of the hammer", close_gripper=True)
    # Once the gripper is around the handle of the hammer, move the hammer above the nail.
    if check("the robot's gripper is around the handle of the hammer"):
        robot.move_gripper("above the nail")
    # Lastly, swing the hammer down onto the nail by opening the gripper.
    # The weight of the hammer should make it fall down onto the nail.
    if check("the robot's gripper is above the nail"):
        robot.move_gripper("above the hammer")  # Reset the gripper position for safety
        robot.move_gripper("near the hammer", close_gripper=False)  # Release the hammer