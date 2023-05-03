
    # Steps:
    #  1. Line up the gripper horizontally with the knob
    #  2. Turn the dial to the right
    #  3. Turn the dial to the left
    # Since the knob is usually in the same relative position on the door, we
    # should line the gripper up horizontally above the knob first.
    if check("the robot's gripper is not horizontally aligned with the knob"):
        robot.move_gripper("horizontally aligned with the knob", close_gripper=True)
    # Now start turning the dial to the right, and then turn it to the left.
    if check("the robot's gripper is horizontally aligned with the knob"):
        robot.move_gripper("above the knob")
        robot.move_gripper("left of the knob")