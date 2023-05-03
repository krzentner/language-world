# Steps:
    #  1. Put gripper above stick
    #  2. Grab the stick with the gripper
    #  3. Bring the gripper to the thermos handle
    #  4. Insert the stick into the thermos handle
    #  5. Pull the thermos to the target location using the stick
    # First, put the gripper above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # If the gripper isn't around the stick, grab it.
    if check("the robot's gripper is not around the stick and the robot's gripper is open"):
        robot.move_gripper("near the stick", close_gripper=True)
    # If the gripper is holding the stick, bring it to the thermos handle.
    if check("the robot's gripper is holding the stick and is not near the thermos handle"):
        robot.move_gripper("near the thermos handle")
    # If the gripper is near the thermos handle, insert the stick into the handle.
    if check("the robot's gripper is near the thermos handle and the stick is not inserted in the handle"):
        robot.move_gripper("around the thermos handle")
    # Once the stick is inserted in the handle, pull the thermos to the target location.
    if check("the stick is inserted in the handle and the robot's gripper is near the target location"):
        robot.move_gripper("near the target location")