
    # Steps:
    #  1. Put gripper above mug
    #  2. Drop gripper around mug
    #  3. Close gripper around mug
    #  4. Pull mug to target
    # First, put the gripper above the mug.
    if check("the robot's gripper is not vertically aligned with mug"):
        robot.put("gripper above mug")
    # Once the gripper is lined up, grab the mug.
    if check("the robot's gripper is vertically aligned with mug and the robot's gripper is not around mug"):
        robot.drop("gripper around mug")
    # If the mug is still near the gripper and open, close the gripper.
    if check("the robot's gripper is near mug and the robot's gripper is open"):
        robot.close("gripper around mug")
    # Now that the mug is trapped, pull it to the target.
    if check("the robot's gripper is above mug and the robot's gripper is closed"):
        robot.pull("mug to goal")