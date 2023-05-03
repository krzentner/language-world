# Steps:
    #  1. Put gripper above the plate
    #  2. Drop gripper around the plate
    #  3. Slide the plate to goal
    # First, put the gripper roughly above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # Once the gripper is roughly above the plate, move it around the plate to
    # grab it.
    if check("the robot's gripper is above the plate and the robot's gripper is open"):
        robot.move_gripper("around the plate", close_gripper=True)
    # Once the gripper is around the plate, slide the plate to the target
    # location.
    if check("the robot's gripper is around the plate and the plate is below the robot's gripper"):
        robot.move_gripper("above the target location")