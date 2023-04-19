
    # Steps:
    #  1. Put gripper above plate
    #  2. Drop gripper around plate
    #  3. Slide the plate to the goal
    # If the gripper is not above the plate, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate", close_gripper=True)
    # If the gripper is above the plate but not around it, then put the gripper
    # around the plate.
    if check("the robot's gripper is above the plate and the robot's gripper is not around the plate"):
        robot.move_gripper("around the plate")
    # Once the gripper is around the plate, we can just slide it to the target
    # location.
    if check("the robot's gripper is around the plate"):
        robot.move_gripper("near the target location")