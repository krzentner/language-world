# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move("gripper above handle")
    if check("the gripper is above handle and the handle is not inside the gripper"):
        robot.grab("handle")
    if check("the gripper is around handle and the handle is not moving"):
        robot.pull("handle up and away from the door")