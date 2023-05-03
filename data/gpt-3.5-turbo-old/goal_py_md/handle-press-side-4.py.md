```
# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    # Steps:
    # 1. Put the gripper near the handle
    # 2. Move the gripper to the side of the handle
    # 3. Push down on the handle
    # First, put the gripper near the handle.
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # Once the gripper is near the handle, move it to the side of the handle.
    if check("the robot's gripper is not to the side of the handle"):
        robot.move_gripper("to the side of the handle")
    # Now that the gripper is to the side of the handle, push down on it.
    if check("the robot's gripper is to the side of the handle"):
        robot.move_gripper("pressing down on the handle")