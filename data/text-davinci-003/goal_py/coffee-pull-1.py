
    # Steps:
    #  1. Put gripper above handle
    #  2. Grab handle with gripper
    #  3. Pull the mug to the target location
    # We want to grab the mug by the handle without bumping it.
    # We should put the gripper above the handle and down the mug so the mug 
    # doesn't get bumped.
    if check("the robot's gripper is not almost vertically aligned with the handle"):
        robot.move_gripper("almost vertically aligned with the handle")
    # Now that the gripper is over the handle, grab the handle and pull.
    if check("the robot's gripper is forward aligned with the handle and the robot's gripper is open"):
        robot.move_gripper("vertically aligned with the handle", close_gripper=True)
    # If the gripper is around the handle, pull the mug to the target location 
    # by moving the gripper.
    if check("the robot's gripper is forward aligned with the handle and the robot's gripper is closed"):
        robot.move_gripper("near the target location")