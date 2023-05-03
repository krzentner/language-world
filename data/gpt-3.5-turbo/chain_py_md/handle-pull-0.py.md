# handle-pull: pull up the handle
def handle_pull(robot):
    # Steps:
    #  1. Put gripper around handle
    #  2. Pick up handle
    #  3. Pull handle up
    # First, put the gripper around the handle.
    if check("the robot's gripper is not around handle"):
        robot.drop("gripper around handle")
    # Once the gripper is around the handle, we can try to pick it up.
    if check("the robot's gripper is around handle and the gripper is open"):
        robot.close("gripper around handle")
    # If the gripper is closed around the handle, try to pull it up.
    if check("the robot's gripper is around handle and the gripper is closed"):
        robot.pull("handle up")