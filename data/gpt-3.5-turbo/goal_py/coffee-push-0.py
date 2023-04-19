# Steps:
    #  1. Put gripper above the mug
    #  2. Grab the mug with the gripper
    #  3. Lift the mug off the table
    #  4. Move the mug to the target location
    #  5. Put the mug down on the target location
    # First, put the gripper above the mug.
    if check("the robot's gripper is not above the mug"):
        robot.move_gripper("above the mug")
    # If the gripper isn't around the mug, put it around the mug.
    if check("the robot's gripper is not around the mug and the robot's gripper is open"):
        robot.move_gripper("near the mug", close_gripper=True)
    # If the gripper is around the mug and the mug is still on the table, lift
    # it off the table.
    if check("the robot's gripper is around the mug and the mug is on the table"):
        robot.move_gripper("above the table")
    # Move the mug to the target location.
    if check("the robot's gripper is not above the target location"):
        robot.move_gripper("above the target location")
    # Put the mug down on the target location.
    if check("the robot's gripper is above the target location and the robot's gripper is closed"):
        robot.move_gripper("on the target location", open_gripper=True)