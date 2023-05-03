# Steps:
    #  1. Put gripper above stick
    #  2. Grab stick with gripper
    #  3. Put gripper above thermos
    #  4. Lower stick to touch thermos lid
    #  5. Push thermos to target location with stick
    # First, put the gripper above the stick to grab it.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # Once the gripper is above the stick, grab it by closing the gripper
    # around it.
    if check("the robot's gripper is above the stick and the gripper is open"):
        robot.move_gripper("around the stick", close_gripper=True)
    # Once the gripper is around the stick, move it above the thermos.
    if check("the robot's gripper is around the stick and the gripper is above the thermos"):
        robot.move_gripper("above the thermos")
    # Lower the stick so that it touches the lid of the thermos.
    if check("the robot's gripper is above the thermos and the stick is not touching the lid of the thermos"):
        robot.move_gripper("touching the lid of the thermos")
    # Once the stick is touching the lid of the thermos, push the thermos to the target location with the stick.
    if check("the robot's gripper is touching the lid of the thermos and the gripper is above the target location"):
        robot.move_gripper("above the target location")