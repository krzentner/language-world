
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Line the handle up with the slot
    #  4. Pull the handle up without getting in the way
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    # If the handle becomes left of the gripper, go back to putting the gripper
    # above the handle.
    # Because the handle is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("handle is not left of the robot's gripper and handle is not forward aligned with the robot's gripper"):
        robot.grab("handle")
    # As long the gripper is still mostly around the handle and the handle isn't
    # lined up with the slot, line up the handle with the slot.
    if check("the robot's gripper is forward aligned with the handle and the handle is not vertically aligned with slot"):
        robot.align("handle to slot")
    # Now that the handle is lined up with the slot, pull it up without getting
    # in the way.
    if check("the handle is vertically aligned with slot"):
        robot.pull("handle up without blocking slot")