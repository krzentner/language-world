# handle-pull: pull up the handle
def handle_pull(robot):
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is not around the handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    if check("the robot's gripper is near the handle and the robot's gripper is open"):
        robot.close("gripper around handle")
    if check("the robot's gripper is around the handle"):
        robot.pull("handle up")