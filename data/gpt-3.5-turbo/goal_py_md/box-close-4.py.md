# box-close: pick up the box lid and place it on the box
def box_close(robot):
    # Steps:
    #  1. Move gripper near the box lid
    #  2. Grab the lid with the gripper
    #  3. Lift the lid and move it above the box
    #  4. Align the lid with the box
    #  5. Lower the lid onto the box
    # First, move the gripper near the box lid.
    if check("the robot's gripper is not near the box lid"):
        robot.move_gripper("near the box lid")
    # Once the gripper is near the box lid, close it to grab the lid.
    if check("the robot's gripper is near the box lid and the robot's gripper is open"):
        robot.move_gripper("around the lid", close_gripper=True)
    # Now that the robot has the lid, lift it and move it above the box.
    if check("the robot's gripper is around the box lid and the robot's gripper is not above the box"):
        robot.move_gripper("above the box")
    # Once the lid is above the box, align it with the box.
    if check("the robot's gripper is above the box and the lid is not aligned with the box"):
        robot.move_gripper("horizontally aligned with the box")
    # Finally, lower the lid onto the box.
    if check("the robot's gripper is horizontally aligned with the box and the lid is above the box"):
        robot.move_gripper("on the box", close_gripper=True)