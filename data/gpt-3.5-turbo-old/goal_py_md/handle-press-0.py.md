# handle-press: push down the handle
# def handle_press(robot):
    # Steps:
    # 1. Put gripper above the handle
    # 2. Grab the handle with the gripper
    # 3. Push down on the handle
    # 4. Release the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the gripper isn't around the handle, put it around the handle.
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.move_gripper("near the handle", close_gripper=True)
    # If the gripper is around the handle and open, push down on the handle.
    # Close the gripper to make sure we keep control of the handle.
    if check("the robot's gripper is around the handle and the robot's gripper is closed"):
        robot.move_gripper("near the handle", push_down=True)
    # If the handle is pushed down, release the handle.
    if check("the handle is pushed down"):
        robot.move_gripper("near the handle", open_gripper=True)