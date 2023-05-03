
    # Steps:
    #  1. Line up gripper as viewed from side
    #  2. Lift up on the handle
    # To start, put the gripper almost vertically aligned with the handle as seen
    # from the side.
    if check("the robot's gripper is not almost vertically aligned with handle as seen from side"):
        robot.move_gripper("almost vertically aligned with handle as seen from side")
    # If the handle is left of the robot's gripper and not lifted, lift up on the
    # handle.
    if check("the handle is not lifted and handle is left of robot's gripper"):
        robot.move_gripper("vertically aligned with handle as seen from side")
    # Once the handle is lifted, we can adjust the robot's gripper position as
    # needed.
    if check("the handle is lifted"):
        robot.move_gripper("above the handle")