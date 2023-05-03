
    # Steps:
    #  1. Put gripper above handle
    #  2. Lift the handle
    #  3. Pull the handle
    # First, thread the robotic arm above the handle, then lower the arm down
    # towards the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    # Once the gripper is roughly above the handle, start lifting it up.
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.lift("handle")
    # Once the handle is lifted a bit, pull the handle up.
    if check("the robot's gripper is near the handle"):
        robot.pull("handle up")