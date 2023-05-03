# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    if check("the robot's gripper is not vertically aligned with the handle and the robot's gripper is not at the side of the handle"):
        robot.move("gripper to side of handle")
    if check("the robot's gripper is at the side of the handle"):
        robot.pull("handle up")