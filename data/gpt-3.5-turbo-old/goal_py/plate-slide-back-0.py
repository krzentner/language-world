# Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Move the gripper back towards the target location
    #  4. Slide the plate into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # Once the gripper is above the plate, grab the plate.
    if check("the robot's gripper is above the plate and the gripper is open"):
        robot.move_gripper("around the plate", close_gripper=True)
    # Move the gripper back toward the target location.
    if check("the robot's gripper is around the plate and not close to the target location"):
        robot.move_gripper("near the target location")
    # Once the gripper is close to the target location, slide the plate into the
    # target location.
    if check("the robot's gripper is near the target location and the plate is still in the gripper"):
        robot.move_gripper("above the target location")