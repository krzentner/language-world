# hammer: hit the nail with the hammer
def hammer(robot):
    # Steps:
    #  1. Put gripper above the hammer handle
    #  2. Grab the handle with the gripper
    #  3. Move the hammer to the nail
    #  4. Lower the hammer and hit the nail
    #  5. Raise the hammer
    # First, put the gripper above the hammer handle.
    if check("the robot's gripper is not vertically aligned with the hammer handle"):
        robot.move_gripper("vertically aligned with the hammer handle")
    # Once the gripper is above the handle, close it to grab the hammer.
    if check("the robot's gripper is vertically aligned with the hammer handle and the robot's gripper is open"):
        robot.move_gripper("around the hammer handle", close_gripper=True)
    # If the gripper now has the hammer, move it to the nail location.
    if check("the robot's gripper is around the hammer handle"):
        robot.move_gripper("near the nail")
    # If the gripper is now above the nail and not too high, lower the hammer to
    # hit the nail.
    if check("the robot's gripper is near the nail and the robot's gripper is not vertically aligned with the nail"):
        robot.move_gripper("vertically aligned with the nail")
    # Once the gripper is lined up with the nail, move it down to hit it.
    if check("the robot's gripper is vertically aligned with the nail"):
        robot.move_gripper("near the nail", close_gripper=True)
    # Hit the nail by raising the hammer and lowering it quickly.
    if check("the robot's gripper is around the nail"):
        robot.move_gripper("vertically aligned with the nail", close_gripper=True)
        robot.move_gripper("near the nail", close_gripper=False)