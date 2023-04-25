
    # Steps:
    #  1. Put the gripper above the lid
    #  2. Drop the gripper around the lid
    #  3. Pick up the lid
    #  4. Place the lid onto the box
    # First, put the gripper above the lid.
    if check("the robot's gripper is not above the lid"):
        robot.put("gripper above lid")
    # If the gripper is not around the lid, try to move it around the lid.
    if check("the robot's gripper is not around the lid and the robot's gripper is open"):
        robot.drop("gripper around lid")
    # If the gripper is around the lid, close it around the lid.
    if check("the robot's gripper is around the lid and the robot's gripper is open"):
        robot.close("gripper around lid")
    # Once the gripper is closed, we can pick up the lid.
    if check("the robot's gripper is around the lid and the robot's gripper is closed"):
        robot.pick("up lid")
    # If we've picked up the lid we can place it back onto the box.
    if check("the robot's gripper is holding the lid"):
        robot.place("lid onto box")