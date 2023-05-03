
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Line the handle up with the slot
    #  4. Pull the handle up from the side
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    # If the handle isn't left of the gripper, grab it.
    # Check if the gripper isn't lined up with it from the front instead of
    # around it.
    if check("handle is not left of the robot's gripper and handle is not forward aligned with the robot's gripper"):
        robot.grab("handle")
    # As long the gripper is still mostly around the handle and the handle isn't
    # lined up with the slot, line up the handle with the slot.
    if check("the robot's gripper is forward aligned with the handle and the handle is not vertically aligned with slot"):
        robot.align("handle to slot")
    # If the handle is aligned with the slot from the side, pull it up.
    if check("handle is vertically aligned with slot"):
        robot.pull("handle up")