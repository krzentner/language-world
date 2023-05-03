
    # Steps:
    #  1. Put gripper near the stick
    #  2. Grab the stick with the gripper
    #  3. Move the stick next to the thermos
    #  4. Push the thermos to the target location with the stick
    # Put the gripper near the stick.
    if check("the robot's gripper is not near the stick"):
        robot.move_gripper("near the stick")
    # Once the gripper is near the stick, the robot can grab it by closing the
    # gripper.
    if check("the robot's gripper is open"):
        robot.move_gripper("around the stick", close_gripper=True)
    # If the gripper is closed and near the stick, move the stick next to the
    # thermos.
    if check("the robot's gripper is not near the thermos"):
        robot.move_gripper("near the thermos")
    # Once the stick is near the thermos, we can push the thermos to the target
    # location with the stick.
    if check("the robot's gripper is near the thermos"):
        robot.move_gripper("above the target location")