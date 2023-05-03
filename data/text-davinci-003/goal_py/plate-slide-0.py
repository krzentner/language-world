
    # Steps:
    #  1. Put gripper near the plate
    #  2. Push down on the plate
    #  3. Slide the plate to goal
    # Just like with pushing the puck, the robot can slide the plate by trapping
    # it between its gripper and the ground.
    # First we should move the gripper near the plate.
    if check("the robot's gripper is not near the plate and the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # Now that the gripper is near the plate, we can push down to trap the plate
    # between the gripper and the ground. If the gripper is closed it won't be
    # able to push down
    if check("the robot's gripper is horizontally aligned with the plate and the robot's gripper is open"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the gripper is trapping the plate, slide it to the goal.
    if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
        robot.move_gripper("near the target location")