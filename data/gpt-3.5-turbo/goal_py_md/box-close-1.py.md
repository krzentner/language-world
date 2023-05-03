# box-close: pick up the box lid and place it on the box
def box_close(robot):
    # Steps:
    #  1. Position the gripper vertically above the box lid
    #  2. Drop the gripper around the box lid
    #  3. Close the gripper around the box lid
    #  4. Lift the box lid
    #  5. Position the gripper vertically above the box
    #  6. Drop the box lid onto the box
    #  7. Release the box lid
    # First, position the gripper vertically above the box lid.
    if check("the robot's gripper is not vertically aligned with the box lid"):
        robot.move_gripper("vertically aligned with the box lid")
    # Once the gripper is aligned, we need to drop it around the box lid.
    # We can do this by moving the gripper around the edges of the box lid until
    # it is fully inside the gripper.
    if check("the robot's gripper is not around the box lid and the robot's gripper is not closed"):
        robot.move_gripper("above the box lid")
        robot.move_gripper("horizontally aligned with the box lid")
        robot.move_gripper("around the box lid", close_gripper=True)
    # Once the gripper is fully around the box lid and has it in a secure grip,
    # we can lift the box lid by raising the gripper.
    if check("the robot's gripper is around the box lid and the robot's gripper is not above the box lid"):
        robot.move_gripper("above the box lid")
    # Now that the box lid is securely held by the gripper, we just need to place
    # it on top of the box.
    # First, we need to position the gripper vertically above the box.
    if check("the robot's gripper is not vertically aligned with the box"):
        robot.move_gripper("vertically aligned with the box")
    # Once the gripper is aligned, we can drop the box lid onto the box by
    # reversing the directions we used to pick it up.
    if check("the robot's gripper is above the box and the robot's gripper is around the box lid"):
        robot.move_gripper("around the box lid")
        robot.move_gripper("horizontally aligned with the box lid")
        robot.move_gripper("around the box", open_gripper=True)