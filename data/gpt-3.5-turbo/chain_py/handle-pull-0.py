# handle-pull: pull up the handle
def handle_pull(robot):
    # Steps:
    #  1. Line up the gripper with the handle
    #  2. Grab the handle
    #  3. Pull up the handle
    # Line up the gripper with the handle, first.
    if check("the robot's gripper is not lined up with the handle"):
        robot.move("gripper to handle")
    # If the gripper is near the handle, we can grab it.
    if check("the robot's gripper is near the handle and the gripper is open"):
        robot.drop("gripper around handle")
    # If the gripper is around the handle, we can pull up on it to lift the
    # handle.
    if check("the robot's gripper is around the handle"):
        robot.pull("the handle up")