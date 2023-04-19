
    # Steps:
    #  1. Put the robot's gripper at front of the plate
    #  2. Slide the plate to the back
    #  3. Slide the plate sideways towards the target
    # To start, we move the robot's gripper to the front of the plate.
    if check("the robot's gripper is not at front of the plate"):
        robot.put("gripper at front of plate")
    # Now that the robot's gripper is at the front of the plate, we can move it
    # back by pushing.
    if check("the robot's gripper is at front of the plate"):
        robot.slide("plate back")
    # Once it's far enough back, we can move it sideways.
    if check("the robot's gripper is behind the plate"):
        robot.slide("plate sideways to target")