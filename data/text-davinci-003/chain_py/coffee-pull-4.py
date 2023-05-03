
    # Steps:
    #  1. Put gripper above the mug handle
    #  2. Drop gripper around mug handle
    #  3. Pull mug towards goal
    # We need to put the gripper above the mug handle before we can grab it.
    if check("the robot's gripper is not vertically aligned with the mug handle"):
        robot.put("gripper above mug handle")
    # Once the gripper is lined up above the mug handle, we should be able to
    # grab the mug handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with the mug handle and the robot's gripper is not around mug handle"):
        robot.put("gripper around mug handle")
    # Once the gripper is around the mug handle, we can just pull the mug
    # towards the goal.
    if check("the robot's gripper is around mug handle"):
        robot.pull("mug towards goal")