# handle-pull: pull up the handle
# def handle_pull(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Close gripper around the handle
    #  3. Pull up the handle
    # First, put the gripper roughly above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle")
    # If the gripper isn't around the handle, put it around the handle.
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.move_gripper("near the handle", close_gripper=True)
    # If the gripper is around the handle and the handle is not in up position, 
    # pull up the handle by moving the gripper up.
    if check("the robot's gripper is around the handle and the handle is not in up position"):
        robot.move_gripper("above the handle", close_gripper=True)