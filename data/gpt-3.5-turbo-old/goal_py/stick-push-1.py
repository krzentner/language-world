    # Steps:
    #  1. Position the stick so that it can push the thermos from the side
    #  2. Push the thermos towards the target location using the stick
    # The stick needs to be positioned to the side of the thermos so that it can
    # push it. We need to move the stick towards the thermos in a straight line
    # to avoid knocking it over.
    if check("the stick is not positioned to the side of the thermos"):
        robot.move_arm("above the stick starting position", gripper_open=True)
        robot.move_arm("above the thermos", gripper_open=True, arm_height='low')
        robot.move_arm("beside the thermos", gripper_open=True)
    # Once the stick is positioned, push the thermos towards the target location
    # using the stick.
    if check("the stick is positioned to the side of the thermos"):
        robot.move_stick("push thermos towards the target location")