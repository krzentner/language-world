
    # Steps:
    #  1. Put gripper above plate
    #  2. Grab the plate with the gripper
    #  3. Line the plate up with the target location
    #  4. Slide the plate back and sideways into the target location
    # If the robot's gripper isn't already above the plate, move it there.
    if check("the robot's gripper is not above plate"):
        robot.move_gripper("above the plate")
    # If the plate isn't left of the gripper, we need to line up the plate with the
    # gripper from the front.
    if check("the plate is not left of the robot's gripper and the plate is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with plate")
    # As long as the plate and the target location aren't lined up to the side,
    # line up the plate and the target location.
    if check("the robot's gripper is forward aligned with the plate and the plate is horizontally aligned with the target location"):
        robot.move_gripper("above the plate")
    # Once the plate is lined up with the target, slide the plate back and
    # sideways.
    if check("the robot's gripper is horizontally aligned with the target location and the plate is not horizontally aligned with the target location"):
        robot.move_gripper("left of the target location")