
    # Steps:
    #  1. Put gripper left of the plate
    #  2. Push the plate from the left
    #  3. Slide the plate back
    # If the plate is right of the robot's gripper, we should move the gripper
    # near the plate to start pushing
    if check("the plate is right of the robot's gripper and the robot's gripper is not near the plate"):
        robot.move_gripper("left of the plate")
    # If the robot's gripper is near the plate we can probably slide the plate
    # back now by moving the gripper left.
    if check("the robot's gripper is near the plate"):
        robot.move_gripper("horizontally aligned with the target location")