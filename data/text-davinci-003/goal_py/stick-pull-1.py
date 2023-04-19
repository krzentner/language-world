
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Push the stick with the gripper
    #  4. Pull the thermos towards the target location
    # First, put the gripper roughly above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around the stick"):
        robot.move_gripper("around the stick")
    # If the stick is above the gripper, we can push the stick to the target
    # location.
    if check("the robot's gripper is near the stick and the stick is below the robot's gripper"):
        robot.move_gripper("near the target location")