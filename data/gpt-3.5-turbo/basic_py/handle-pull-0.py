def handle_pull(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above the handle")
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not around the handle"):
        robot.put("gripper around the handle")
    if check("the robot's gripper is around the handle"):
        robot.pull("the handle up")