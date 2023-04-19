# handle-pull: pull up the handle
# def handle_pull(robot):
    if check("the robot's gripper is not almost vertically aligned with handle"):
        robot.put("gripper above the handle")
    if check("the robot's gripper is almost vertically aligned with the handle and the robot's gripper is open"):
        robot.put("gripper around handle")
        robot.close("gripper around handle")
    if check("the robot's gripper is around handle and the handle is in down position"):
        robot.pull("handle up")