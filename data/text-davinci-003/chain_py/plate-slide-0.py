
    # Steps:
    #  1. Put gripper above plate
    #  2. Push gripper into top of plate
    #  3. Slide plate to goal
    # Plate sliding is similar to puck sliding. We just need to make sure the
    # gripper is above the plate so we can trap it with the gripper.
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above the plate")
    # Once the gripper is lined up, the robot can trap the plate by pushing it
    # down slightly.
    if check("the robot's gripper is above the plate and robot's gripper is not near the plate"):
        robot.push("down on plate")
    # Once the gripper is near the plate, we can start sliding it to the target
    # location.
    if check("the robot's gripper is near the plate"):
        robot.slide("plate to goal")