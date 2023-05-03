def handle_pull(robot):
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above the handle")
    if check("the robot's gripper is above the handle and the robot's gripper is not around the handle"):
        robot.drop("gripper around the handle")
    if check("the robot's gripper is around the handle"):
        robot.pull("up on the handle")