# Steps:
    #  1. Put gripper above mug handle
    #  2. Drop gripper around mug handle
    #  3. Close gripper around mug handle
    #  4. Move mug to goal location
    # First, put the gripper above the mug handle.
    if check("the robot's gripper is not vertically aligned with mug handle"):
        robot.put("gripper above mug handle")
    # If the gripper isn't around the mug handle, put it around the handle.
    if check("the robot's gripper is vertically aligned with mug handle and the robot's gripper is not around mug handle"):
        robot.drop("gripper around mug handle")
    # If the gripper is around the mug handle and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is around mug handle and the robot's gripper is open"):
        robot.close("gripper around mug handle")
    # We closed the gripper, and the mug is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the mug to the goal location.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is around mug handle and the robot's gripper is closed and the mug is not at the goal location"):
        robot.move("mug to goal location")