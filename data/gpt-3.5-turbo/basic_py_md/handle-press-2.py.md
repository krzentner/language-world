# handle-press: push down the handle
def handle_press(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not around the handle"):
        robot.grab("handle")
    if check("the robot's gripper is around the handle"):
        robot.push("down on handle")