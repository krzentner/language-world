# hammer: hit the nail with the hammer
def hammer(robot):
    # Steps:
    #  1. Position the gripper over the hammer
    #  2. Close the gripper around the hammer
    #  3. Position the gripper over the nail
    #  4. Hit the nail with the hammer
    # Position the gripper over the hammer
    if check("the robot's gripper is not vertically aligned with the hammer"):
        robot.move_gripper("vertically aligned with the hammer")
    # Close the gripper around the hammer
    if check("the robot's gripper is vertically aligned with the hammer"):
        robot.move_gripper("around the hammer", close_gripper=True)
    # Position the gripper over the nail
    if check("the robot's gripper is not near the nail"):
        robot.move_gripper("near the nail")
    # Hit the nail with the hammer
    if check("the robot's gripper is near the nail"):
        robot.move_gripper("onto the nail", hammer=True)