
    # Steps:
    #  1. Put gripper left of the plate
    #  2. Slide the plate back sideways
    # We need to put the gripper left of the plate first before we can start
    # sliding it sideways.
    if check("the robot's gripper is in front of the plate or the robot's gripper is almost vertically aligned with the plate"):
        robot.move_gripper("left of the plate")
    # If the robot's gripper is left of the plate, we can start sliding it
    # sideways by moving the gripper in the same direction.
    if check("the robot's gripper is left of the plate"):
        robot.move_gripper("behind the plate")
    # If the plate is almost back, just keep pushing sideways.
    if check("the robot's gripper is behind the plate and the plate is not almost back"):
        robot.move_gripper("behind the target location")