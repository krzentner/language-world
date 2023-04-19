# hammer: hit the nail with the hammer
# def hammer(robot):
    # Steps:
    #  1. Put gripper above hammer
    #  2. Drop gripper around handle
    #  3. Close gripper around handle
    #  4. Put gripper above the nail
    #  5. Open gripper to release hammer onto nail
    #  6. Move gripper away from the nail to lift the hammer
    # First, put the gripper roughly above the hammer handle so we don't knock the hammer over.
    if check("the robot's gripper is not above the hammer"):
        robot.move_gripper("above the hammer")
    # Once the gripper is above the handle, put it around the hammer handle.
    if check("the robot's gripper is not around the hammer handle and the robot's gripper is open"):
        robot.move_gripper("near the hammer handle", close_gripper=True)
    # Once the gripper is around the handle, move it above the nail.
    if check("the robot's gripper is around the hammer handle"):
        robot.move_gripper("above the nail", close_gripper=False)
    # Once the gripper is above the nail, open the gripper to release the hammer.
    if check("the robot's gripper is above the nail and the gripper is closed around the hammer handle"):
        robot.move_gripper("above the nail", close_gripper=False)
    # Once the gripper is no longer holding the hammer, move the gripper away from the nail.
    if check("the robot's gripper is not near the hammer handle"):
        robot.move_gripper("above the hammer")