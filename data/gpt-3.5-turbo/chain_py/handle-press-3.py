# Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Push gripper down to press handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.place("gripper above handle")
    # If the gripper isn't around the handle, put it around the handle.
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    # If the gripper is near the handle and open, maybe we can press it by
    # pushing down the gripper.
    if check("the robot's gripper is near handle and the robot's gripper is open"):
        robot.push("down on the handle with the gripper")