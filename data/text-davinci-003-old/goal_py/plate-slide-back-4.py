
    # Steps:
    #  1. Put gripper above the plate
    #  2. Drop the gripper around the plate
    #  3. Slide the plate back
    # To start moving the plate, we need to put the gripper above it.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # Once the gripper is above the plate, put it around the plate.
    if check("the robot's gripper is not around the plate and the robot's gripper is open"):
        robot.move_gripper("around the plate", close_gripper=True)
    # Once the gripper is around the plate, easily slide it back
    if check("the robot's gripper is around the plate"):
        robot.move_gripper("near the target location")