# handle-pull: pull up the handle
def handle_pull(robot):
    # Steps:
    #  1. Put gripper around the handle
    #  2. Pull up the handle
    # First, put the gripper around the handle.
    if check("the robot's gripper is not around the handle"):
        robot.move_gripper("around the handle")
    # Once the gripper is around the handle, we can just pull it up.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("above the handle")