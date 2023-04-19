
    # Steps:
    #  1. Put gripper forward of plate
    #  2. Grip plate
    #  3. Align plate with target location
    #  4. Push plate into target location
    # If the robot's gripper is not near the plate, put the gripper near the
    # plate.
    if check("the robot's gripper is not near the plate"):
        robot.put("gripper forward of plate")
    # If the robot's gripper is near the plate, try to grab it.
    if check("the robot's gripper is near the plate and the robot's gripper is open"):
        robot.grab("plate")
    # If the robot's gripper is gripping the plate, align the plate with the
    # target location.
    if check("the robot's gripper is gripping the plate and the plate is not horizontally aligned with the target location"):
        robot.align("plate with target location")
    # If the plate is aligned with the target location, push it into the target
    # location.
    if check("the plate is horizontally aligned with the target location"):
        robot.push("plate into target location")