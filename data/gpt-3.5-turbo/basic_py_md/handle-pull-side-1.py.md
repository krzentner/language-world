# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("handle is not aligned with the robot's gripper and the robot's gripper is open"):
        robot.move("gripper to side of handle")
    if check("the robot's gripper is around the handle and the handle is not pulled up"):
        robot.pull("handle up")