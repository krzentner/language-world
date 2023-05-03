
    # Steps:
    #  1. Put gripper above mug handle
    #  2. Drop gripper around mug handle
    #  3. Close gripper around mug handle
    #  4. Move mug to goal
    # First, move the gripper above the handle of the mug
    if check("the robot's gripper is not above mug handle and the robot's gripper is not forward aligned with mug handle"):
        robot.put("gripper above the mug handle")
    # If the gripper is forward aligned but not around the mug, try to grab it.
    if check("the robot's gripper is forward aligned with mug handle and the robot's gripper is open"):
        robot.drop("gripper around mug handle")
    # If the robot's gripper is closed around the mug handle, we should be able
    # to move the mug.
    if check("the robot's gripper is around mug handle and the robot's gripper is closed"):
        robot.move("mug to goal")