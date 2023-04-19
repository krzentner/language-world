# handle-press: push down the handle
# def handle_press(robot):
    # Steps:
    #  1. Align the gripper above the handle
    #  2. Close the gripper around the handle
    #  3. Push down on the handle
    # First, put the gripper directly above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the gripper is above the handle and open, grab the handle by closing
    # the gripper.
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is open"):
        robot.move_gripper("around the handle", close_gripper=True)
    # Once the gripper is around the handle, push down on it.
    if check("the robot's gripper is closed around the handle"):
        robot.move_gripper("downward pressure on the handle")