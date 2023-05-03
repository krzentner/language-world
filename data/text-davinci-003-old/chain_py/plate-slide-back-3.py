
    # Steps:
    #  1. Put gripper above the plate
    #  2. Slide the plate back
    # The plate is a relatively large object, so we need to line up the gripper
    # with the plate from above.
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    # If the plate is the correct direction from the gripper, we can slide it
    # back.
    if check("the robot's gripper is above the plate"):
        robot.slide("plate back")