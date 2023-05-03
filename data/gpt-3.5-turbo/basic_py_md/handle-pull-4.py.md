# handle-pull: pull up the handle
def handle_pull(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is almost vertically aligned with the handle and the robot's gripper is open"):
        robot.put("gripper around handle")
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.pull("handle up")