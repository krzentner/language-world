
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Push the thermos to the goal
    # Put the gripper above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # Once the gripper is above the stick, grab the stick by closing the
    # gripper.
    if check("the robot's gripper is above the stick and the robot's gripper is open"):
        robot.move_gripper("forward aligned with the stick", close_gripper=True)
    # If we've grabbed the stick, we can push the thermos.
    if check("the robot's gripper is forward aligned with the stick"):
        robot.move_gripper("near the thermos")