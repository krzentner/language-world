# Steps:
    #  1. Put gripper above the box lid
    #  2. Grab the box lid with the gripper
    #  3. Move gripper above the box
    #  4. Release the box lid on top of the box
    # First, put the gripper above the box lid.
    if check("the robot's gripper is not above the box lid"):
        robot.move_gripper("above the box lid")
    # If the gripper is above the box lid, grab the box lid with the gripper.
    if check("the robot's gripper is above the box lid and the robot's gripper is open"):
        robot.move_gripper("around the box lid", close_gripper=True)
    # If the gripper is holding the lid and not above the box, move the gripper
    # above the box.
    if check("the robot's gripper is holding the box lid and the robot's gripper is not above the box"):
        robot.move_gripper("above the box")
    # If the gripper is above the box, release the box lid on top of the box.
    if check("the robot's gripper is above the box and holding the box lid"):
        robot.move_gripper("above the box lid", close_gripper=False)