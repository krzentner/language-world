# handle-pull: pull up the handle
def handle_pull(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Pull up on the handle
    # First, position the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # Once the gripper is lined up with the handle, close the gripper around
    # the handle.
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is open"):
        robot.move_gripper("around the handle")
    # With the gripper around the handle, pull up on the handle.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("above the handle")