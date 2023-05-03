# Steps:
    #  1. Put gripper above the handle of the mug
    #  2. Grab the handle of the mug with the gripper
    #  3. Tilt the mug to prevent spilling
    #  4. Move the mug to the target location
    # First, put the gripper roughly above the mug's handle, so that we don't
    # knock the mug over while trying to grab it.
    if check("the robot's gripper is not above the handle of the mug"):
        robot.put("gripper above mug handle")
    # Once the gripper is above the handle of the mug, we can grab it.
    if check("the robot's gripper is above the handle of the mug and the robot's gripper is not around the handle of the mug"):
        robot.grab("mug handle")
    # We need to tilt the mug to prevent spilling while it's being moved.
    if check("the mug is not tilted"):
        robot.tilt("mug")
    # Once the mug is tilted, we can move it to the target location.
    if check("the mug is tilted"):
        robot.move("mug to goal")