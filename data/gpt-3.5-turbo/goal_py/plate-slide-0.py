# Steps:
    #  1. Put gripper above plate
    #  2. Drop gripper around plate
    #  3. Close gripper around plate
    #  4. Slide plate to goal
    # We can slide the plate by picking it up and holding it horizontally, then
    # moving it to the target location.
    # If the gripper isn't above the plate, move it there.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the gripper isn't around the plate, put it there.
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the gripper is holding the plate, move it to the target location by
    # sliding it.
    if check("the robot's gripper is holding the plate"):
        robot.move_gripper("above the target location")