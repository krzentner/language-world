# handle-pull: pull up the handle
# def handle_pull(robot):
    # Steps:
    #  1. Put gripper around the handle
    #  2. Pull up the handle
    # First, move the gripper near the handle.
    if check("the robot's gripper is not near the handle"):
        robot.move("gripper to handle")
    # Once the gripper is near the handle, put it around the handle.
    if check("the robot's gripper is not around the handle"):
        robot.drop("gripper around handle")
    # If the gripper is around the handle, we can pull up the handle.
    if check("the robot's gripper is around the handle"):
        robot.pull("handle up")