
    # Steps:
    #  1. Put gripper around mug handle
    #  2. Push mug to target
    # If the robot's gripper is not near the handle, move it near the handle.
    if check("the robot's gripper is not near mug handle"):
        robot.move_gripper("above the mug handle")
    # Close the gripper to hold onto the mug.
    if check("the robot's gripper is near mug handle and is open"):
        robot.move_gripper("around the mug handle", close_gripper=True) 
    # Once the gripper is around the mug handle, we can just slide the mug to
    # the target location.
    if check("the robot's gripper is around mug handle"):
        robot.move_gripper("above the target location")