
    # Steps:
    #  1. Put gripper above the box lid
    #  2. Drop gripper around box lid
    #  3. Grab the box lid
    #  4. Raise box lid in the air
    #  5. Move box lid above the box
    #  6. Lower box lid onto box
    #  7. Release box lid
    # We start by putting the gripper above the box lid, to avoid bumping it while
    # lowering the gripper.
    if check("the robot's gripper is not above the box lid"):
        robot.put("gripper above box lid")
    # If the gripper isn't around the box lid, put it around the box lid.
    if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
        robot.drop("gripper around box lid")
    # If the gripper is near the box lid, maybe we can grab the box lid by
    # closing the gripper.
    # We're doing this early, since the box lid will probably fall out of the
    # gripper if we don't.
    if check("the robot's gripper is near the box lid and the robot's gripper is open"):
        robot.grab("box lid")
    # If the box lid is above the gripper, we can probably grab it.
    if check("the box lid is above the robot's gripper"):
        robot.raise("box lid above robot's gripper")
    # If the robot's gripper is above the box lid, we can move the box lid above
    # the box.
    if check("the robot's gripper is above box lid and the box lid is above the robot's gripper"):
        robot.move("box lid above box")
    # If the robot's gripper is aligned with the box, we should probably lower the
    # box lid onto the box.
    # Then, we'll go back to trying to grab the box lid.
    if check("the robot's gripper is horizontally aligned with box"):
        robot.put("box lid onto box")
    # If the robot's gripper is aligned with the box and the box lid is below the
    # robot's gripper, we can probably release the