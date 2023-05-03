# Steps:
    #  1. Put gripper near dial
    #  2. Turn dial to the desired position
    # We don't need to be too precise in positioning the gripper around the dial.
    if check("the robot's gripper is not at the dial"):
        robot.move_gripper("near the dial")
    # Once the gripper is near the dial, we can turn it to the desired position.
    if check("the robot's gripper is at the dial"):
        robot.move_gripper("dial turned to the desired position")