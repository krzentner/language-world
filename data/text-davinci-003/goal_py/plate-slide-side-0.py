
    # Steps:
    #  1. Put gripper left of plate
    #  2. Touch plate with gripper
    #  3. Slide plate left in a continuous motion
    # The robot can slide the plate by trapping it with the gripper.
    # If the plate isn't left of the gripper, move the gripper near the plate.
    if check("the robot's gripper is not left of the plate and the robot's gripper is not near the plate"):
        robot.move_gripper("near the plate")
    # If the gripper is near the plate but not touching it, close the gripper
    # to trap it.
    if check("the robot's gripper is near the plate and the robot's gripper is open "):
        robot.move_gripper("left of the plate", close_gripper=True)
    # If the gripper is touching the plate, slide the plate to the target
    # location.
    if check("the robot's gripper is touching the plate"):
        robot.move_gripper("horizontally aligned with the target location")