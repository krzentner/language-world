# plate-slide: slide the plate into the target location
# def plate_slide(robot):
    # Steps:
    #  1. Put the gripper on one end of the plate
    #  2. Push the plate towards the target
    #  3. Repeat until the plate is at the target location
    # First, we need to find out which end of the plate is closer to the target.
    # If the robot's gripper is not on one end of the plate, move it to one end.
    if check("the robot's gripper is not on the end of the plate"):
        robot.put("gripper on one end of the plate")
    # While the plate is not yet at the target location, keep pushing it towards
    # the target.
    while check("the plate is not yet at the target location"):
        robot.push("the plate towards the target")