# Steps:
    #  1. Put gripper above the box lid
    #  2. Grab the box lid
    #  3. Move the lid above the box
    #  4. Lower the lid onto the box
    # First, put the gripper above the box lid.
    if check("the robot's gripper is not above the box lid"):
        robot.put("gripper above the box lid")
    # If the gripper isn't around the box lid yet, open it and move it around
    # the box lid.
    if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
        robot.move("gripper around the box lid")
    # Once the gripper is around the box lid, grab it.
    if check("the robot's gripper is around the box lid and the robot's gripper is open"):
        robot.close("gripper around the box lid")
    # Now move the box lid above the box.
    if check("the robot's gripper is holding the box lid and the box lid is not above the box"):
        robot.move("lid above the box")
    # Finally, lower the lid onto the box.
    if check("the robot's gripper is holding the box lid and the box lid is above the box"):
        robot.place("lid onto the box")