
    # Steps:
    #  1. Put gripper above lid
    #  2. Drop gripper around lid
    #  3. Close the gripper around lid
    #  4. Place lid on the box
    # First, we need to put the gripper above the box lid.
    if check("the robot's gripper is not above lid"):
        robot.put("gripper above lid")
    # If the gripper is above the lid, but not around it, try to drop it around
    # the lid.
    if check("the robot's gripper is above the lid and the robot's gripper is not around the lid and the robot's gripper is open"):
        robot.drop("gripper around lid")
    # If the gripper is around the lid, we're likely close to closing the gripper
    # around the lid, so just close it.
    if check("the robot's gripper is around the lid and the robot's gripper is open"):
        robot.close("gripper around lid")
    # Once the gripper is around the lid, we can just move the lid to the box
    # and place it.
    if check("the robot's gripper is around the lid and the robot's gripper is closed"):
        robot.place("lid on box")