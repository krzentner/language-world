# box-close: pick up the box lid and place it on the box
# def box_close(robot):
    # Steps:
    #  1. Put gripper above the box lid
    #  2. Grab the box lid with the gripper
    #  3. Lift the box lid off the top of the box
    #  4. Move the box lid on top of the box
    #  5. Release the box lid
    # First, put the gripper above the box lid.
    if check("the robot's gripper is not vertically aligned with the box lid"):
        robot.put("gripper above box lid")
    # If the gripper isn't around the box lid, put it around the box lid.
    if check("the robot's gripper is not around box lid and the robot's gripper is open"):
        robot.drop("gripper around box lid")
    # If the gripper is near the box lid and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near box lid and the robot's gripper is open"):
        robot.close("gripper around box lid")
    # We closed the gripper, and the box lid is still near the gripper, so maybe we
    # grabbed it.
    # Try to lift the box lid off the top of the box.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is holding onto the box lid"):
        robot.lift("box lid")
    # If the box lid is held up by the gripper, move it on top of the box.
    if check("the robot's gripper is holding the box lid above the box"):
        robot.move("box lid above the box")
    # If the box lid is in place, release the gripper.
    if check("the box lid is on top of the box"):
        robot.release("gripper")