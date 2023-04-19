# handle-pull: pull up the handle
# def handle_pull(robot):
    if check("the robot's gripper is not above door handle and the robot's gripper is vertically aligned with the door handle"):
        robot.move("the gripper above the door handle")
    if check("the robot's gripper is above the door handle"):
        robot.grab("the door handle")
    if check("the door handle is not pulled up"):
        robot.pull("up on the door handle")