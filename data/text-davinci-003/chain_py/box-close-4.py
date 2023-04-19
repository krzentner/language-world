
    # Steps:
    #  1. Put gripper above the lid
    #  2. Drop gripper around the lid
    #  3. Close gripper around the lid
    #  4. Pick up lid
    #  5. Move to the box
    #  6. Place the lid on the box
    # First, put the gripper roughly above lid, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the lid"):
        robot.place("gripper above lid")
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
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above lid and the robot's gripper is closed"):
        robot.move("lid to the box")
    # If the gripper is near the box, try to place the lid on the box.
    if check("the robot's gripper is near the box"):
        robot.place("lid on box")