
    # Steps:
    #  1. Put gripper above front of plate
    #  2. Push gripper into top of plate
    #  3. Slide plate backward towards goal
    # We don't want to just trap the plate, because we need to be careful not to
    # bump it and knock it onto the ground.
    # So first, accurately place the gripper above the plate.
    if check("the robot's gripper is not above the plate and the robot's gripper is not in front of the plate"):
        robot.put("the gripper above the plate")
    # As long as the gripper is in front of the plate, but not above it, try to
    # move it above the plate.
    if check("the robot's gripper is in front of the plate"):
        robot.put("the gripper above the plate")
    # If the gripper is above the plate, close the gripper slightly so that we
    # don't lose control of the plate.
    if check("the robot's gripper is above the plate and the robot's gripper is open"):
        robot.close("gripper slightly")
    # As long as the gripper is above the plate, slide the plate backwards towards
    # the goal.
    if check("the robot's gripper is above the plate and the robot's gripper is closed"):
        robot.slide("plate back towards goal")