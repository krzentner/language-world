
    # Steps:
    #  1. Put gripper behind plate
    #  2. Grab plate with gripper
    #  3. Slide plate back
    # First, move the gripper behind the plate.
    if check("the robot's gripper is not behind the plate"):
        robot.put("gripper behind plate")
    # If the robot's gripper is near the plate, we should be able to grab it by
    # closing the gripper.
    if check("the robot's gripper is near plate and the robot's gripper is open"):
        robot.grab("plate with gripper")
    # Now that the plate is in the robot's gripper, slide it back as necessary.
    if check("the robot's gripper is behind plate and the robot's gripper is closed"):
        robot.slide("plate back")