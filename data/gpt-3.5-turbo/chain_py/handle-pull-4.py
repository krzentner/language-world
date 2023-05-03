# handle-pull: pull up the handle
def handle_pull(robot):
    # Steps:
    #  1. Put gripper around handle
    #  2. Pull up on the handle
    # We need to put the gripper around the handle before we can pull it up.
    # As long as the gripper is not around the handle, we should put the
    # gripper around it.
    if check("the robot's gripper is not around handle"):
        robot.grab("handle")
    # Now that the gripper is around the handle, we can pull up on it.
    if check("the robot's gripper is around handle"):
        robot.pull("up on handle")