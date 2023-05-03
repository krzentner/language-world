# Steps:
    #  1. Put gripper above mug handle
    #  2. Grab mug handle with gripper
    #  3. Lift mug
    #  4. Move mug to target location
    #  5. Lower mug
    # First, line up the gripper above the mug handle.
    if check("the robot's gripper is not vertically aligned with the mug handle"):
        robot.put("gripper above mug handle")
    # Once the gripper is lined up, grab the mug handle.
    if check("the robot's gripper is vertically aligned with the mug handle and the robot's gripper is not gripping the mug handle"):
        robot.grip("mug handle")
    # Now that we're holding the mug handle, lift the mug.
    if check("the robot's gripper is gripping the mug handle and the mug is not lifted"):
        robot.lift("mug")
    # Move the mug to the target location.
    if check("the mug is lifted"):
        robot.slide("mug to goal")
    # Finally, once the mug is in position, lower it.
    if check("the mug is at goal"):
        robot.lower("mug")