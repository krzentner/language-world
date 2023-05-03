
    # Steps:
    #  1. Put gripper above wrench handle
    #  2. Grab the wrench handle with the gripper
    #  3. Pull the wrench off of the peg
    # If the gripper isn't above the wrench handle, move the gripper above the
    # wrench handle.
    # This might be tricky since the wrench and peg are often close together, so
    # we might need to move the gripper carefully.
    if check("the robot's gripper is not above wrench handle"):
        robot.put("gripper above wrench handle")
    # We should now grab the wrench handle if it's close, so move it if needed.
    if check("the robot's gripper is not around wrench handle and the robot's gripper is near wrench handle"):
        robot.grab("wrench handle")
    # If the gripper is now around the wrench handle, try to pull it off.
    if check("the robot's gripper is around wrench handle"):
        robot.pull("wrench away from peg")