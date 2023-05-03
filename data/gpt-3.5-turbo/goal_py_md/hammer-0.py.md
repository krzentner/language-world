# hammer: hit the nail with the hammer
def hammer(robot):
    # Steps:
    #  1. Put gripper above the hammer
    #  2. Grab the hammer with the gripper
    #  3. Move the hammer above the nail
    #  4. Swing the hammer down to hit the nail
    # First, position the gripper above the hammer.
    if check("the robot's gripper is not above the hammer"):
        robot.move_gripper("above the hammer")
    # Once the gripper is above the hammer, close it to grab the hammer.
    if check("the robot's gripper is above the hammer and the robot's gripper is open"):
        robot.move_gripper("near the hammer", close_gripper=True)
    # After grabbing the hammer, move it to above the nail.
    if check("the robot's gripper is holding the hammer and the hammer is not above the nail"):
        robot.move_gripper("above the nail")
    # Finally, swing the hammer down to hit the nail.
    if check("the robot's gripper is holding the hammer and the hammer is above the nail"):
        robot.move_gripper("onto the nail", swing_hammer=True)