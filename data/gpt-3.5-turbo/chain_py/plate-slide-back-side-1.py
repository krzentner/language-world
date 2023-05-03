# Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Slide the plate sideways towards target
    # First, align the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above the plate")
    # Once the gripper is above the plate, grab the plate.
    if check("the robot's gripper is above the plate and the robot's gripper is open"):
        robot.grab("the plate")
    # Once the gripper is around the plate, slide the plate towards the target.
    # The plate needs to be slid sideways since the target is on the side of the
    # plate.
    if check("the robot's gripper is around the plate"):
        robot.slide("the plate sideways to the target")