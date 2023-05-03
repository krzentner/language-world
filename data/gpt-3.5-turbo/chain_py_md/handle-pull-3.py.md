# handle-pull: pull up the handle
def handle_pull(robot):
    # Steps:
    #  1. Put gripper around the handle
    #  2. Apply a pulling force to lift up the handle
    # First, move the gripper to be close to the handle.
    if check("the robot's gripper is not near the handle"):
        robot.move("gripper to handle")
    # Align the gripper with the handle.
    if check("the robot's gripper is not around the handle"):
        robot.drop("gripper around handle")
    # Apply a force to lift up the handle.
    if check("the robot's gripper is around handle"):
        robot.pull("up on handle")