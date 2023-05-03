
    # Steps:
    #  1. Put gripper above mug handle
    #  2. Drop gripper around mug handle
    #  3. Pull mug towards goal
    # We need to put the gripper near the mug handle before we can grab it.
    if check("the robot's gripper is not vertically aligned with mug handle"):
        robot.put("gripper above mug handle")
    # As long as the gripper isn't around the mug handle, close it.
    if check("the robot's gripper is vertically aligned with mug handle and the robot's gripper is not around mug handle"):
        robot.drop("gripper around mug handle")
    # As long as the gripper is near the mug, pull the mug to the goal.
    if check("the robot's gripper is near mug handle and the mug is below the robot's gripper"):
        robot.pull("mug to goal")