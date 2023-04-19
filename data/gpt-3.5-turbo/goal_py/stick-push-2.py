# Steps:
    #  1. Pick up the stick
    #  2. Put the stick next to the thermos
    #  3. Push the thermos to the target location
    # First, we need to pick up the stick. If the gripper is not open, open it.
    if check("the robot's gripper is not open"):
        robot.move_gripper("open")
    # If the stick is not in the robot's gripper, position the gripper above it
    # and close the gripper around it.
    if check("the robot's gripper is open and the stick is not in the robot's gripper"):
        robot.move_gripper("above the stick", close_gripper=True)
    # If the stick is in the gripper, we can move the gripper to the vicinity of
    # the thermos.
    if check("the stick is in the robot's gripper"):
        robot.move_gripper("next to the thermos")
    # With the stick next to the thermos, we can use it to push the thermos to
    # the target location.
    if check("the robot's gripper is next to the thermos"):
        robot.move_gripper("near the target location")