
    # Steps:
    #  1. Put gripper above box lid
    #  2. Drop gripper around box lid
    #  3. Close gripper around box lid
    #  4. Lift box lid
    #  5. Place box lid on box
    # First, put the gripper about above the box lid so we can grab it.
    if check("the robot's gripper is not above the box lid and the robot's gripper is not vertically aligned with the box lid"):
        robot.put("gripper above box lid")
    # If the box lid is lined up, close the gripper around it.
    if check("the robot's gripper is vertically aligned with the box lid and the robot's gripper is not around box lid"):
        robot.drop("gripper around box lid")
    # After the gripper is closed around the box lid, we should be able to lift
    # the box lid.
    if check("the robot's gripper is around box lid"):
        robot.lift("box lid")
    # Lift the box lid and put it on the box.
    if check("the robot's gripper is above the box lid"):
        robot.place("box lid on box")