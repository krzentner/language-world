# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    if check("the robot's gripper is not vertically aligned with the handle and the gripper is not either right or left of the handle"):
        robot.move("gripper right of handle")
    if check("the robot's gripper is right of the handle and the robot's gripper is not vertically aligned with the handle"):
        robot.move("gripper above handle")
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.pull("handle up from side")