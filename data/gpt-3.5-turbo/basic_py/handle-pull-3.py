# handle-pull: pull up the handle
def handle_pull(robot):
    if check("the robot's gripper is not near the handle"):
        robot.grab("handle")
    if check("the robot's gripper is aligned with the handle"):
        robot.pull("handle up")