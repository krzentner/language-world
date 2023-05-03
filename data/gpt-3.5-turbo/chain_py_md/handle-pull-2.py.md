# handle-pull: pull up the handle
def handle_pull(robot):
    # Steps:
    #  1. Put gripper around handle
    #  2. Lift up the handle
    # First, put the gripper roughly around the handle.
    if check("the robot's gripper is not around the handle"):
        robot.move("gripper to handle")
        robot.drop("gripper around handle")
    # Once the gripper is around the handle, lift it up.
    if check("the robot's gripper is around handle"):
        robot.pull("up on handle")