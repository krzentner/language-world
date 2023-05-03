
    # Steps:
    #  1. Put gripper above plate
    #  2. Push gripper into side of plate
    #  3. Slide plate sideways to goal
    # The plate is long, so it's easy to slide by trapping it's side in the
    # gripper.
    # If the plate is not right of the gripper as seen in front, move the
    # gripper above the plate.
    if check("the robot's gripper is not right of plate or not front aligned with plate"):
        robot.put("gripper above plate")
    # If the plate is right of the gripper as seen in front, but the gripper
    # isn't around the plate, push the gripper into the plate.
    if check("the robot's gripper is right of plate and the robot's gripper is not around plate"):
        robot.push("gripper into side of plate")
    # If the gripper is around the plate, we can slide it by moving the gripper.
    # Close the gripper to make sure we keep control of the plate.
    if check("the robot's gripper is around plate"):
        robot.slide("plate sideways to goal")