# handle-pull: pull up the handle
# def handle_pull(robot):
    if check("the robot's gripper is not above handle"):
        robot.place("gripper above handle")
    if check("the robot's gripper is not around handle and the gripper is open"):
        robot.drop("gripper around handle")
    if check("the robot's gripper is near handle and the gripper is open"):
        robot.close("gripper around handle")
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")