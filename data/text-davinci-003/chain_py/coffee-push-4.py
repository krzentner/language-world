
    # Steps:
    #  1. Put gripper around the mug handle
    #  2. Close the gripper
    #  3. Push the mug to the target location
    # First, move the gripper around the mug handle.
    if check("the robot's gripper is not around the mug handle and the robot's gripper is open"):
        robot.grab("mug handle")
    # Once the gripper is around the mug handle, close it to trap the mug.
    if check("the robot's gripper is around the mug handle and the robot's gripper is open"):
        robot.close("gripper around mug handle")
    # Once the mug is trapped in the gripper, slide it to the goal.
    if check("the robot's gripper is around the mug handle and the robot's gripper is closed"):
        robot.slide("mug to goal")