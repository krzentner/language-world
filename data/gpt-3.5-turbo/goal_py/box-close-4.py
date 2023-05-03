# Steps
    #  1. Move gripper above the box lid
    #  2. Drop gripper around the box lid
    #  3. Close gripper around the lid
    #  4. Move gripper above the box
    #  5. Drop the lid on top of the box
    #  6. Release the lid
    # First, put the gripper roughly above the box lid, so that we don't bump it while trying to grab it
    if check("the robot's gripper is not above the box lid"):
        robot.move_gripper("above the box lid")
    # If the gripper isn't around the box lid, put it around the box lid
    if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
        robot.move_gripper("around the box lid", close_gripper=True)
    # Move the gripper above the box
    if check("the robot's gripper is not above the box"):
        robot.move_gripper("above the box")
    # Place the box lid on the box
    if check("the robot's gripper is above the box"):
        # Lower the gripper until the box lid is touching the box
        robot.move_gripper("touching the box")
        # Release the box lid
        robot.move_gripper("above the box", open_gripper=True)