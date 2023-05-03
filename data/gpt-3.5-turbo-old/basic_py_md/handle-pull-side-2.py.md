# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    if check("the robot's gripper is not vertically aligned with the handle and the robot's gripper is not on the same side as the handle"):
        robot.move("gripper to same side as handle")
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with handle"):
        robot.grab("handle")
    if check("the handle is not up"):
        robot.pull("handle up")