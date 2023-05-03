
    # Steps:
    #  1. Put gripper above plate
    #  2. Grab plate with gripper
    #  3. Slide plate back
    # In order to push directly on the plate with the gripper, we need to put the
    # gripper above the plate.
    if check("the robot's gripper is not above plate"):
        robot.move_gripper("above the plate")
    # Once the gripper is above the plate, grab the plate.
    # This is because the robot has to control the plate by grabbing it.
    if check("the robot's gripper is above plate and the robot's gripper is not around the plate"):
        robot.move_gripper("around the plate")
    # Once the gripper is around the plate, slide the plate back.
    if check("the robot's gripper is around the plate"):
        robot.move_gripper("above the target location")