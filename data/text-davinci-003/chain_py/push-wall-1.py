
    # Steps:
    #  1. Align the gripper with the corner between the wall and the target
    #  2. Push the wall away from the target location
    #  3. Slide the puck to the target location
    # If the gripper is not right at the corner between the wall and the target,
    # move it there.
    if check("the robot's gripper is not at the corner between the wall and the target"):
        robot.align("gripper at corner")
    # If the gripper is at the corner, push the wall away from the target so that
    # we can slide the puck there.
    if check("the robot's gripper is at corner"):
        robot.push("wall away from target")
    # Now that the wall is pushed away from the target, we can slide the puck to
    # the target.
    if check("wall is away from target"):
        robot.slide("puck to target")