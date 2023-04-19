# handle-press: push down the handle
# def handle_press(robot):
    if check("the robot's gripper is not positioned above the handle"):
        robot.move("the gripper above the handle")
    if check("the robot's gripper is positioned above the handle and the gripper is not closed"):
        robot.close("on the handle")
    if check("the gripper is closed around the handle"):
        robot.push("down on the handle")