# coffee-pull: grab the mug and pull it to the target location
# def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above the mug handle
    #  2. Drop gripper around the handle
    #  3. Grab the handle
    #  4. Move the handle to the target location by pulling it
    # First, put the gripper above the mug handle.
    if check("the robot's gripper not above the mug handle"):
        robot.move_gripper("above the mug handle")
    # If the gripper isn't around the handle, put it around the handle.
    if check("the robot's gripper is not around the mug handle and the robot's gripper is open"):
        robot.move_gripper("near the mug handle", close_gripper=True)
    # If the gripper is near the handle and open, grab it by closing the gripper.
    if check("the robot's gripper is around the mug handle and the robot's gripper is open"):
        robot.move_gripper("grabbing the mug handle", close_gripper=True)
    # If the handle is grabbed and not yet at the target location, pull it to the target location.
    if check("the robot's gripper is grabbing the mug handle and the mug handle is not at the target location"):
        robot.move_gripper("near the target location", force_pull=True)