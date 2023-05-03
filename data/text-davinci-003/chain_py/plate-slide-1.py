
    # Steps:
    #  1. Put gripper near the plate
    #  2. Push gripper into side of plate
    #  3. Slide plate to goal
    # The robot can slide the plate by trapping it by pushing in from the side and
    # moving the gripper.
    # If the robot isn't close enough to the plate to trap it, move the gripper
    # to the side of the plate.
    if check("the robot's gripper is not near the plate"):
        robot.put("the gripper near the plate")
    # If the robot is close enough to the plate, but not trapping it, trap the
    # plate.
    if check("the robot's gripper is not trapping the plate"):
        robot.push("the gripper into the plate")
    # Now that we have trapped the plate, we can slide it.
    if check("the robot's gripper is trapping the plate"):
        robot.slide("the plate to goal")