# Steps:
    #  1. Put gripper on top of the plate
    #  2. Push the plate back into the target location
    # We can slide the plate back by pushing down on it with the gripper.
    # First, move the gripper above the plate.
    if check("the robot's gripper is not above the plate" and "the plate is not in the target location"):
        robot.move_gripper("above the plate")
    # If the gripper is above the plate, move it down to push the plate back.
    if check("the robot's gripper is above the plate"):
        robot.move_gripper("near the plate")