# hammer: hit the nail with the hammer
# def hammer(robot):
    # Steps:
    #  1. Put the gripper above the hammer
    #  2. Close the gripper around the handle of the hammer
    #  3. Move the gripper above the nail
    #  4. Rotate the gripper to position the hammer a certain way
    #  5. Move the gripper downward to hit the nail
    #  6. Lift the gripper and release the hammer
    # First, put the gripper above the hammer.
    if check("the robot's gripper is not vertically aligned with the hammer"):
        robot.move_gripper("vertically aligned with the hammer")
    # If the gripper isn't around the hammer, close the gripper around the handle.
    if check("the robot's gripper is not around the hammer and the robot's gripper is open"):
        robot.move_gripper("near the hammer", close_gripper=True)
    # If the gripper is around the hammer, move the gripper above the nail.
    if check("the robot's gripper is around the hammer and the robot's gripper is not above the nail"):
        robot.move_gripper("above the nail")
    # If the gripper is above the nail, rotate the gripper to position the hammer correctly.
    if check("the robot's gripper is above the nail and the hammer is not positioned correctly"):
        robot.rotate_gripper("positioned correctly")
    # Move the gripper downwards to hit the nail with the hammer.
    if check("the hammer is not touching the nail"):
        robot.move_gripper("touching the nail")
    # Lift the gripper and release the hammer.
    if check("the robot's gripper is touching the nail"):
        robot.move_gripper("above the nail", open_gripper=True)