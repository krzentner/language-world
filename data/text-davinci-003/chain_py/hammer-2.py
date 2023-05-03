
    # Steps:
    #  1. Put gripper above the hammer handle
    #  2. Drop the gripper around the hammer handle
    #  3. Pull back the hammer
    #  4. Align above the nail and swing the hammer
    # First, the gripper should line up vertically with the handle of the hammer.
    if check("the robot's gripper is not above the hammer handle"):
        robot.put("the gripper above the hammer handle")
    # If the gripper isn't wrapped around the handle, grab it by moving the
    # gripper around the handle.
    if check("the robot's gripper is not around the hammer handle"):
        robot.grab("the hammer handle")
    # If the gripper is vertically aligned with the handle and the gripper is
    # closed, pull the hammer back so that we can hit the nail.
    if check("the robot's gripper is vertically aligned with the hammer handle and the robot's gripper is closed"):
        robot.pull("back the hammer")
    # If the gripper is still vertically aligned with the hammer handle and the
    # gripper is closed, align the hammer handle over the nail and swing.
    if check("the robot's gripper is vertically aligned with the hammer handle and the robot's gripper is closed"):
        robot.swing("hammer")