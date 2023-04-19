# coffee-pull: grab the mug and pull it to the target location
# def coffee_pull(robot):
    # Steps:
    #   1. Put gripper above the handle of the mug
    #   2. Grab the handle of the mug
    #   3. Line up the mug with the target location
    #   4. Pull the mug towards the target location
    # First, put the gripper above the handle of the mug.
    if check("the robot's gripper is not vertically aligned with the mug handle"):
        robot.put("gripper above the mug handle")
    # If the gripper is not around the mug handle, grab the handle.
    if check("the robot's gripper is not around the mug handle"):
        robot.grab("the mug handle")
    # While the mug is not horizontally aligned with the target location, align it.
    if check("the mug is not horizontally aligned with the target location"):
        robot.align("mug to target")
    # If the mug is aligned with the target location, pull it towards the target.
    if check("the mug is horizontally aligned with the target location and the robot's gripper is near the mug handle"):
        robot.pull("the mug towards the target location")