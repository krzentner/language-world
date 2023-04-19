
    # Steps:
    #  1. Put gripper around plate
    #  2. Slide plate sideways
    # First, we need to put the gripper around the plate for control and to make
    # sure we can slide it.
    if check("the robot's gripper is not around plate"):
        robot.put("gripper around plate")
    # Once the gripper is around the plate, try to slide it sideways to the
    # target location.
    if check("the robot's gripper is around plate"):
        robot.slide("plate sideways")