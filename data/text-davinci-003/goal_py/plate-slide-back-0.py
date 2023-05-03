
    # Steps:
    #  1. Put gripper in back of plate
    #  2. Slide plate back
    # Put the gripper in the back of the plate.
    if check("the robot's gripper is not behind plate"):
        robot.move_gripper("back of the plate")
    # Slide the plate back.
    if check("the robot's gripper is behind plate"):
        robot.move_gripper("near the target location")