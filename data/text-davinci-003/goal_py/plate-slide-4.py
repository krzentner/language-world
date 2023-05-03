
    # Steps:
    #  1. Put gripper on one side of plate
    #  2. Push plate to goal
    # First, line up the robot's gripper along the side of the plate.
    if check("the robot's gripper is not horizontally aligned with the plate"):
        robot.move_gripper("left of the plate")
    # Then, move the gripper to the side to start pushing the plate.
    # We'll open the gripper to get a better grip.
    if check("the robot's gripper is horizontally aligned with the plate"):
        robot.move_gripper("near the plate", close_gripper=False)
    # Now push the plate to the goal.
    if check("the robot's gripper is near the plate"):
        robot.move_gripper("forward aligned with the plate")