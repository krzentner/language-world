# Steps:
    #  1. Put gripper near the plate
    #  2. Push the plate towards the target location
    # To slide the plate, we just need to push it with the gripper.
    # If the gripper is not near the plate, move it near.
    if check("the robot's gripper is not near plate"):
        robot.move_gripper("near the plate")
    # If the gripper is near the plate, push it to the target location.
    if check("the robot's gripper is near the plate"):
        robot.move_gripper("above the target location")