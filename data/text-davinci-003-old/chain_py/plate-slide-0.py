
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Slide the plate to the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # As long as the plate isn't forward aligned with the gripper, we can grab
    # it.
    if check("the plate is not forward aligned with the robot's gripper and the robot's gripper is open"):
        robot.grab("plate")
    # If the plate is forward aligned with the gripper and the gripper is closed,
    # we have the plate.
    # Try to slide it to the target location.
    # If it's not sliding, just go back to an earlier step.
    if check("the plate is forward aligned with the robot's gripper and the robot's gripper is closed"):
        robot.slide("plate to target location")