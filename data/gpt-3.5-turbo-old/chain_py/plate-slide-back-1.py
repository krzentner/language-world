# Steps:
    #  1. Put gripper above plate
    #  2. Grab plate with gripper
    #  3. Move plate back to target location
    # We first need to put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # Once the gripper is lined up above the plate, we can grab the plate.
    if check("the robot's gripper is vertically aligned with plate and the robot's gripper is open"):
        robot.grab("plate")
    # Now that the plate is secured by the gripper, we can slide the plate back
    # to the target location.
    if check("the plate is secure in the gripper and the gripper is not near the target location"):
        robot.slide("plate back to target location")