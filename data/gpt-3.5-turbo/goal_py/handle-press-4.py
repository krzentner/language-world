# Steps:
    #  1. Move gripper above handle
    #  2. Drop gripper around handle
    #  3. Push handle down
    # First, move the gripper above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle")
    # If the gripper is not around the handle, move it around the handle.
    if check("the robot's gripper is not around the handle"):
        robot.move_gripper("around the handle", close_gripper=True)
    # Once the gripper is around the handle, push it down to complete the task.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("downward pressure on the handle")