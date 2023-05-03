# handle-press: push down the handle
# def handle_press(robot):
    if check("the robot's gripper is not almost vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is almost vertically aligned with the handle and the robot's gripper is open"):
        robot.put("gripper around handle")
    if check("the robot's gripper is around handle"):
        robot.push("down on handle")