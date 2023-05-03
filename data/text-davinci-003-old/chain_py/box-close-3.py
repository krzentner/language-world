
    # Steps:
    #  1. Put gripper above the box lid
    #  2. Grab the box lid with the gripper
    #  3. Lift the box lid
    #  4. Move the box lid to the box
    #  5. Place the box lid onto the box
    # First, put the gripper above the box lid.
    if check("the robot's gripper is not above the box lid"):
        robot.put("gripper above box lid")
    # If the gripper is not around the box lid, try to close the gripper around
    # it.
    if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
        robot.drop("gripper around box lid")
    # If the gripper closed around the box lid, we're ready to lift it.
    if check("the robot's gripper is around the box lid and the robot's gripper is closed"):
        robot.lift("box lid")
    # Now that the box lid is lifted, move it to the box.
    if check("the box lid is lifted"):
        robot.move("box lid to box")
    # Place the box lid on the box.
    if check("the box lid is above the box"):
        robot.place("box lid on box")