
    # Steps:
   #  1. Put gripper above box lid
    #  2. Drop gripper around box lid
    #  3. Close gripper around box lid
    #  4. Line up box lid with box
    #  5. Place box lid on the box
    # To close the box we need to first pick up the lid.
    # Put the gripper above the lid:
    if check("the robot's gripper is not above box lid"):
        robot.put("gripper above box lid")
    # Drop the gripper around the box lid:
    if check("the robot's gripper is not around box lid and the robot's gripper is open"):
        robot.drop("gripper around box lid")
    # Close the gripper to grab the box lid:
    if check("the robot's gripper is around box lid and the robot's gripper is open"):
        robot.close("gripper around box lid")
    # If the box lid is mostly off the box, line up the box lid with the box. We
    # don't need to worry about the direction of the lid, because the box is
    # much bigger than the lid.
    if check("box lid is off box and the robot's gripper is forward aligned with box lid"):
        robot.place("box lid with box")
    # If the box lid is lined up with the box, start placing it on the box.
    if check("box lid is aligned with box"):
        robot.place("box lid on box")