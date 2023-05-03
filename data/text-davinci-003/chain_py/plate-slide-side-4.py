
    # Steps:
    #  1. Put gripper at an angle above the plate
    #  2. Line up the plate so the gripper is just to the side
    #  3. Slide the plate sideways into the goal
    # If the gripper isn't above the plate, move the gripper to the plate as seen
    # from the right side.
    # Because the object is large, we don't have to be especially careful about
    # the gripper going mostly above the plate.
    if check("the robot's gripper is not within angle of the plate"):
        robot.grab("plate from right")
    # If the gripper is within an angle of the plate, the plate should start to
    # be on the side of the gripper and the gripper should be lined up with the
    # goal.
    # Close the gripper to trap the plate and then slide the plate to the goal.
    if check("the plate is to the side of the robot's gripper and the robot's gripper is forward left aligned with the goal"):
        robot.close("gripper around plate")
        robot.slide("plate to goal")