# Steps:
    #  1. Put gripper near the edge of the plate nearest to the target location
    #  2. Push the plate to the target location from the side
    # If the gripper is not near the edge of the plate closest to the target
    # location, position it there.
    if check("the robot's gripper is not near the edge of the plate closest to the target location"):
        robot.move_gripper("near the edge of the plate closest to the target location")
    # If the gripper is near the edge of the plate, we can start pushing the plate
    # sideways to the target location.
    if check("the robot's gripper is near the edge of the plate closest to the target location"):
        robot.move_gripper("horizontally aligned with the target location")