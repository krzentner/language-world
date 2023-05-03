# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    if check("the robot's gripper is not close to the handle"):
        robot.move("gripper to the side of the handle")
        robot.move("gripper near the handle")
    if check("the robot's gripper is still not holding the handle"):
        robot.grab("handle")
    if check("the gripper is holding the handle and the handle is not moved"):
        robot.pull("the handle up")