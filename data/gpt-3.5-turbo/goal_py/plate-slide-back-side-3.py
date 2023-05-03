# Steps:
    #  1. Put gripper roughly above the plate
    #  2. Drop gripper around the back edge of the plate
    #  3. Push the plate sideways to the target location
    # First, put the gripper above the plate, roughly lined up with the back edge.
    if check("the robot's gripper is not vertically aligned with the back edge of the plate"):
        robot.move_gripper("vertically aligned with the back edge of the plate")
    # If the gripper isn't around the back edge of the plate, drop it around.
    if check("the robot's gripper is not around the back edge of the plate"):
        robot.move_gripper("around the back edge of the plate")
    # Once the gripper is around the back edge of the plate, we can push it
    # sideways to the target location.
    if check("the robot's gripper is around the back edge of the plate and near the target location"):
        robot.move_gripper("horizontally aligned with the target location")