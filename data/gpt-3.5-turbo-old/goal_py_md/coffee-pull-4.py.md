# coffee-pull: grab the mug and pull it to the target location
# def coffee_pull(robot):
    # Steps:
    #  1. Put gripper around the mug handle
    #  2. Align the mug with the target location
    #  3. Pull the mug to the target location
    # First, put the gripper around the mug handle.
    if check("the robot's gripper is not around the mug handle and the robot's gripper is open"):
        robot.move_gripper("near the mug handle", close_gripper=True)
    # If the gripper is around the mug handle, line up the mug with the target location.
    if check("the robot's gripper is around the mug handle and the mug is not aligned with the target location"):
        robot.move_gripper("above the mug", close_gripper=True)
        robot.move_gripper("vertically aligned with the target location", close_gripper=True)
    # If the mug is lined up with the target location, pull it there.
    if check("the robot's gripper is vertically aligned with the target location"):
        robot.move_gripper("above the target location", close_gripper=True)