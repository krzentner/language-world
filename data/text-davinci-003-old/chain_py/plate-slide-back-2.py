
    # Steps:
    #  1. Put gripper above the plate
    #  2. Drop gripper around the plate
    #  3. Slide the plate back
    # If the gripper is not behind the plate, put the gripper above the plate.
    if check("the robot's gripper is not behind the plate"):
        robot.put("gripper above plate")
    # If the gripper is above and left or right of the plate, put it around
    # the plate.
    if check("the robot's gripper is above the plate and the robot's gripper is left-aligned with or right-aligned with the plate"):
        robot.drop("gripper around plate")
    # Once the gripper is around the plate, just slide it backwards until it's
    # in the target location.
    if check("the robot's gripper is around the plate"):
        robot.slide("plate back")