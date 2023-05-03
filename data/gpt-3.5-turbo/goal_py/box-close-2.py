# Steps:
    #  1. Put gripper above the box lid
    #  2. Drop gripper around the box lid
    #  3. Close the gripper around the box lid
    #  4. Move the lid to the top of the box
    #  5. Open the gripper to release the lid
    # First, put the gripper above the box lid.
    if check("the robot's gripper is not above the box lid"):
        robot.move_gripper("above the box lid")
    # If the gripper isn't around the box lid, put it around the box lid.
    if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
        robot.move_gripper("near the box lid", close_gripper=True)
    # If the gripper is near the box lid and open, maybe we can grab it by closing
    # the gripper.
    if check("the box lid is not below the robot's gripper"):
        robot.move_gripper("above the box")
    # If the box lid is above the box and the gripper is closed, place the box lid on the box
    if check("the robot's gripper is above the box lid and horizontally aligned with the box lid"):
        robot.move_gripper("above the box lid", close_gripper=False)