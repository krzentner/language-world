# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not around the handle"):
        robot.grab("handle sideways")
    if check("the robot's gripper is around the handle"):
        robot.pull("up on handle")