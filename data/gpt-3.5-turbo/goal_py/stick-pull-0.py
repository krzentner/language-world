# Steps:
    #  1. Put gripper above the stick near the end we want to use to pull
    #  2. Close gripper around the stick
    #  3. Put the gripper around the thermos
    #  4. Use the stick to pull the thermos to the target location
    # First, put the gripper above the stick near the end we want to use to pull,
    # which should be closer to the thermos.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # If the gripper is above the stick, close it around the stick to grab it.
    if check("the robot's gripper is above the stick and the gripper is open"):
        robot.move_gripper("around the stick", close_gripper=True)
    # Once we've grabbed the stick, move the gripper to the thermos and put it
    # around the thermos.
    if check("the robot's gripper is not around the thermos and the gripper is closed"):
        robot.move_gripper("around the thermos")
    # Once we've put the gripper around the thermos with the stick, we can use
    # the stick to pull the thermos to the target location.
    if check("the robot's gripper is around the thermos"):
        robot.move_gripper("near the target location")