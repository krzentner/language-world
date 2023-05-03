# handle-pull: pull up the handle
def handle_pull(robot):
    if check("the robot's gripper is not near the handle"):
        robot.move("gripper above handle")
    if check("the robot's gripper is above the handle and the robot's gripper is open"):
        robot.close("gripper around handle")
    if check("the robot's gripper is around the handle and the handle is facing upwards"):
        robot.pull("handle up")