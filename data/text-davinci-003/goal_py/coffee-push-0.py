
    # Steps:
    #  1. Put gripper forward of the mug
    #  2. Push gripper into side of mug
    #  3. Slide mug to goal
    # The robot can slide the mug by trapping it in the gripper and moving the
    # gripper.
    # If the mug isn't to the side of the gripper, move the gripper to the side
    # of the mug.
    if check("the robot's gripper is not forward aligned with mug"):
        robot.move_gripper("forward aligned with the mug", close_gripper=True)
    # If the gripper is forward aligned but not near the mug, move gripper close
    #  to the mug to trap it.
    if check("the robot's gripper is near the mug"):
        robot.move_gripper("lightly to the side of the mug", close_gripper=True)
    # Once the mug is trapped, slide it to the target location.
    if check("the robot's gripper is near the mug"):
        robot.move_gripper("above the target location")