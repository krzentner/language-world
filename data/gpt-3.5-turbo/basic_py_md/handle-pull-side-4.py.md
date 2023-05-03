# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("handle is not left of the robot's gripper and handle is not forward aligned with the robot's gripper"):
        robot.grab("handle")
    if check("the robot's gripper is forward aligned with the handle and the handle is not vertically aligned with the lock"):
        robot.move("gripper above lock")
    if check("the robot's gripper is above the lock and the handle is not inserted into the lock"):
        robot.align("handle with lock")
    if check("handle is inserted into lock and the robot's gripper is holding the handle"):
        robot.pull("up on the handle")