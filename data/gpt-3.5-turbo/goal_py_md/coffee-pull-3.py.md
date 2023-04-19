# coffee-pull: grab the mug and pull it to the target location
# def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above the mug handle
    #  2. Grab the handle with the gripper
    #  3. Pull the mug towards the target location
    # First, put the gripper above the mug handle.
    if check("the robot's gripper is not vertically aligned with mug handle"):
        robot.move_gripper("vertically aligned with the mug handle")
    # If the gripper is above the mug handle, grab the handle.
    if check("the robot's gripper is vertically aligned with mug handle and the robot's gripper is open"):
        robot.move_gripper("around the mug handle", close_gripper=True)
    # If the gripper has successfully grabbed the mug, pull it towards the target location.
    if check("the robot's gripper is around the handle and the mug is not at the target location"):
        robot.move_gripper("above the target location")