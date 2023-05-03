# Steps:
    #  1. Put gripper on side of plate
    #  2. Slide gripper behind plate
    #  3. Push plate sideways into target location
    # We can slide the plate back by putting the gripper on the side of the
    # plate and pushing it sideways.
    # First, put the gripper on the side of the plate, away from the target
    # location.
    if check("the robot's gripper is not on the side of the plate"):
        robot.move_gripper("on the side of the plate")
    # Once the gripper is on the side, we can slide it behind the plate.
    if check("the robot's gripper is on the side of the plate and the robot's gripper is not behind the plate"):
        robot.move_gripper("behind the plate")
    # Once the gripper is behind the plate, push it sideways into the target
    # location.
    if check("the robot's gripper is behind the plate and the plate is not in the target location"):
        robot.move_gripper("horizontally aligned with the target location")