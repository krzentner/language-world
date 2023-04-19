# handle-pull: pull up the handle
# def handle_pull(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Grab handle
    #  3. Pull handle up
    # First, put the gripper mostly above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle")
    # If the gripper isn't around the handle, put it around the handle.
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
    	robot.move_gripper("near the handle", close_gripper=True)
    # If the gripper is around the handle and close, we can pull the handle up.
    if check("the robot's gripper is around handle and the gripper is closed"):
    	robot.move_gripper("above the handle and then pull the handle up")