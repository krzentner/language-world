# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    # Steps:
    #  1. Move the gripper right of the handle
    #  2. Put the gripper around the handle
    #  3. Move the handle upwards
    # First, move the gripper to the right of the handle.
    if check("the robot's gripper is not right of the handle"):
        robot.move_gripper("right of the handle")
    # If the gripper is not around the handle, put it around the handle.
    if check("the robot's gripper is not around the handle and the robot's gripper is open"):
        robot.move_gripper("near the handle", close_gripper=True)
    # If the gripper is around the handle, move the handle upwards.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("above the handle")