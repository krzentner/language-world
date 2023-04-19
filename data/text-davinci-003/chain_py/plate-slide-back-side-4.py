
    # Steps:
    #  1. Put gripper close to bottom of plate
    #  2. Orient the plate with the target position
    #  3. Push the back of the plate back into the target position
    # We'll want to put the gripper near the bottom of the plate before we start
    # manipulating it.
    if check("the robot's gripper is not near bottom of plate"):
        robot.put("gripper close to bottom of plate")
    # After lining up the gripper, we want to orient the plate with the target
    # position. We don't want the plate to overshoot or undershoot our target.
    if check("the plate is not aligned with the target"):
        robot.align("plate with the target")
    # After the plate is in the target position, we just have to push the back
    # of the plate back into the target position.
    if check("the plate is aligned with the target"):
        robot.push("the back of the plate back into the target")