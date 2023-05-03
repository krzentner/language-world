# coffee-pull: grab the mug and pull it to the target location
# def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above the mug's handle
    #  2. Grab the handle with the gripper
    #  3. Pull the mug to the target location
    # First, put the gripper above the mug's handle
    if check("the robot's gripper is not vertically aligned with the mug's handle"):
        robot.put("gripper above mug's handle")
    # If the gripper is not completely around the mug's handle, move it around
    # the handle.
    if check("the robot's gripper is not around the mug's handle and the robot's gripper is open"):
        robot.drop("gripper around mug's handle")
    # Check if the gripper is now completely around the handle
    if check("the robot's gripper is near the mug's handle and the robot's gripper is not closed"):
        robot.close("gripper around mug's handle")
    # If the mug is now held by the gripper, pull it to the target location
    if check("the robot's gripper is holding the mug and the mug is not at the target location"):
        robot.pull("mug to target location")