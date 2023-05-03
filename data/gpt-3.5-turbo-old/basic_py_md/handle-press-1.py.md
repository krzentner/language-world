# handle-press: push down the handle
# def handle_press(robot):
    if check("the robot's gripper is not above and aligned vertically with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is above and aligned vertically with the handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    if check("the robot's gripper is around the handle and the robot's gripper is open"):
        robot.close("gripper around handle")
    if check("the robot's gripper is around the handle and the robot's gripper is closed"):
        robot.push("down on handle")