# Steps:
    #  1. Put gripper above the box lid
    #  2. Grab the lid with the gripper
    #  3. Move the lid above the box
    #  4. Release the lid by opening the gripper
    # First, put the gripper above the box lid.
    if check("the robot's gripper is not vertically aligned with the box lid"):
        robot.move_gripper("vertically aligned with the box lid")
    # Next, grab the lid with the gripper.
    if check("the robot's gripper is vertically aligned with the box lid and the gripper is open"):
        robot.move_gripper("around the box lid")
    # Once the lid is in the gripper, move it above the box.
    if check("the robot's gripper is around the box lid"):
        robot.move_gripper("above the box", close_gripper=True)
    # Finally, release the lid onto the box by opening the gripper.
    if check("the robot's gripper is above the box and the gripper is closed"):
        robot.move_gripper("vertically aligned with the box lid", close_gripper=False)