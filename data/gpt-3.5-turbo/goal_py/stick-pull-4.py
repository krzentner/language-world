# Steps:
    #  1. Put the gripper on the stick
    #  2. Put the stick in the thermos handle
    #  3. Pull the stick towards the target location
    # First, put the gripper around the stick.
    if check("the robot's gripper is not around the stick, and the robot's gripper is open"):
        robot.move_gripper("around the stick", close_gripper=True)
    # If the gripper is around the stick, put the stick into the thermos handle.
    if check("the robot's gripper is around the stick, and the stick is not in the thermos handle"):
        robot.move_gripper("in the thermos handle")
    # Once the stick is in the thermos handle, pull the stick towards the target
    # location.
    if check("the stick is in the thermos handle, and the robot's gripper is at the target location"):
        robot.move_gripper("pull the stick")