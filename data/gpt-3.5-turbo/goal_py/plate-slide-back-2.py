# Steps:
    #  1. Put gripper above the plate
    #  2. Drop gripper around the plate
    #  3. Slide the plate back
    # We should start with the gripper above the plate to make sure it doesn't
    # bump into anything while moving in.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # Once the gripper is above the plate, we can drop it around the plate to
    # pick it up.
    if check("the robot's gripper is above the plate and the robot's gripper is not around the plate"):
        robot.move_gripper("near the plate", close_gripper=True)
    # With the plate gripped, we can slide it back into its target location.
    if check("the robot's gripper is around the plate and the plate is not in the target location"):
        robot.move_gripper("above the target location")