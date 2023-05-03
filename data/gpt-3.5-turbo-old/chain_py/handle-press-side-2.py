# Steps:
    #  1. Put gripper left of the handle
    #  2. Grab the handle with the gripper
    #  3. Push down on the handle from the side
    # First, put the gripper left of the handle
    if check("the robot's gripper is not left of the handle"):
        robot.move("gripper to left of handle")
    # If the gripper is not around the handle, grab it
    if check("the robot's gripper is left of handle and the robot's gripper is open"):
        robot.grab("handle")
    # If the gripper is gripping the handle and not pushing down, push down on it
    if check("the robot's gripper is gripping the handle and the handle is not pressed down"):
        robot.push("down on handle from side")