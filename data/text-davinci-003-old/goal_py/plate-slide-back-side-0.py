
    # Steps:
    #  1. Put gripper in front of plate
    #  2. Push plate back sideways
    # If the robot's gripper is not near the plate, move it to the plate.
    if check("the robot's gripper is not near the plate"):
        robot.move_gripper("near the plate")
    # If the plate is not left of the robot's gripper, move the plate left.
    if check("plate is not left of the robot's gripper and plate is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the plate", close_gripper=True)
    # As long the gripper is still mostly around the plate and the plate isn't
    # lined up with the target location, line up the plate with the target
    # location.
    if check("plate is horizontally aligned with target location"):
        robot.move_gripper("left of the plate")
    # If the plate is lined up with the target location to the side, insert it.
    if check("the robot's gripper is forward aligned with the plate and the plate is not horizontally aligned with target location"):
        robot.move_gripper("horizontally aligned with target location")