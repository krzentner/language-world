
    # Steps:
    #  1. Put gripper above the mug handle
    #  2. Grab the mug handle with the gripper
    #  3. Lift the mug up
    #  4. Pull the mug to the target location
    # First, put the gripper above the mug handle, so that we don't bump into it
    # as we try to grab it.
    if check("the robot's gripper is not above the mug handle"):
        robot.put("gripper above mug handle")
    # If the gripper is lined up above the mug handle, move it down to the mug
    # handle.
    if check("the robot's gripper is vertically aligned with the mug handle and the  robot's gripper is not around mug handle"):
        robot.grab("mug handle")
    # If the gripper is near the mug handle, close it to grab it.
    if check("the robot's gripper is near the mug handle and the robot's gripper is open"):
        robot.close("gripper around mug handle")
    # Once the gripper is closed, lift the mug.
    if check("the robot's gripper is around the mug handle"):
        robot.lift("mug up")
    # We lifted the mug, so we can pull it to the target location.
    if check("the robot's gripper is above mug and the mug is below the robot's gripper"):
        robot.pull("mug to the target location")