# handle-pull: pull up the handle
# def handle_pull(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Pull the handle up
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the gripper is above the handle, grab it.
    if check("the robot's gripper is above the handle and the robot's gripper is open"):
        robot.move_gripper("around the handle", close_gripper=True)
    # Once the gripper is around the handle, lift the handle up.
    if check("the robot's gripper is around the handle and the robot's gripper is not vertically aligned with the goal"):
        robot.move_gripper("vertically aligned with the goal")
    # Finally, move the gripper to the goal location while lifting the handle.
    if check("the robot's gripper is vertically aligned with the goal"):
        robot.move_gripper("near the goal location")