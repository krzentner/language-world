
    # Steps:
    #  1. Put gripper above mug handle
    #  2. Drop gripper around mug handle
    #  3. Pull mug to goal
    # First, put the gripper above the mug handle.
    if check("the robot's gripper is not vertically aligned with the mug handle"):
        robot.put("gripper above mug handle")
    # As long as the gripper is aligned with the mug handle and not near it, move
    # the gripper down to the mug handle.
    if check("the robot's gripper is vertically aligned with the mug handle and the robot's gripper is open"):
        robot.put("gripper around mug handle")
    # As long as the gripper is still around the mug handle, pull the mug towards
    # the target location.
    if check("the robot's gripper is around mug handle"):
        robot.pull("mug to goal")