# handle-pull: pull up the handle
def handle_pull(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the gripper is not around the handle"):
        robot.grab("handle")
    if check("the handle is not pulled up"):
        robot.pull("handle up")