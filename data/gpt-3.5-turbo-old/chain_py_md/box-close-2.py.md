# box-close: pick up the box lid and place it on the box
# def box_close(robot):
    # Steps:
    #  1. Put gripper above the box lid
    #  2. Grab the box lid with the gripper
    #  3. Move the gripper to the box
    #  4. Drop the box lid on the box
    # Put the gripper above the box lid.
    if check("the robot's gripper is not above the box lid"):
        robot.place("gripper above the box lid")
    # If the gripper isn't around the box lid, put it around the box lid.
    if check("the robot's gripper is not around box lid and the robot's gripper is open"):
        robot.drop("gripper around box lid")
    # If the gripper is near the box lid and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near box lid and the robot's gripper is open"):
        robot.close("gripper around box lid")
    # We closed the gripper, and the box lid is still near the gripper, so maybe we
    # grabbed it.
    # Move the gripper to the box.
    if check("the robot's gripper is above the box lid and the robot's gripper is closed"):
        robot.move("gripper to the box")
    # Drop the box lid on the box.
    if check("the robot's gripper is above the box"):
        robot.drop("box lid on the box")