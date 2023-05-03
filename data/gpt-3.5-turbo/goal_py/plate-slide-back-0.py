# Steps:
    #  1. Put gripper near front of plate
    #  2. Push plate back into target location
    # The robot can slide the plate back by gripping it near the front and
    # pushing it back into the target location.
    # If the gripper isn't near the front of the plate, move it there.
    # We don't need to be especially accurate with our alignment.
    if check("the robot's gripper is not near the front of the plate"):
        robot.move_gripper("near the front of the plate")
    # If the gripper is near the front of the plate, we can probably slide it
    # back by pushing.
    if check("the robot's gripper is near the front of the plate and the robot's gripper is not at the target location"):
        robot.move_gripper("at the target location", close_gripper=True)