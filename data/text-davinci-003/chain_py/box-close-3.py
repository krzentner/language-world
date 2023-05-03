
    # Steps:
    #  1. Put gripper above the lid
    #  2. Drop gripper around the lid
    #  3. Close gripper around the lid
    #  4. Move lid to the box
    #  5. Place lid on the box
    # First, put the gripper above the lid.
    if check("the robot's gripper is not above lid"):
        robot.put("gripper above lid")
    # If the gripper isn't around the lid, put it around the lid.
    if check("the robot's gripper is not around lid and the robot's gripper is open"):
        robot.drop("gripper around lid")
    # If the gripper is near the lid and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near lid and the robot's gripper is open"):
        robot.close("gripper around lid")
    # We closed the gripper, and the lid is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the lid to the box.
    if check("the robot's gripper is above lid and the robot's gripper is closed"):
        robot.move("lid to box")
    # If the lid is over the box and the gripper is still closed, place it
    # carefully on the box.
    if check("the lid is over the box and the robot's gripper is closed"):
        robot.place("lid on box")