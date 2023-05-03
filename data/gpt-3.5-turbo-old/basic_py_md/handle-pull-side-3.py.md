# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
   if check("the robot's gripper is not vertically aligned with the handle and the robot's gripper is not near the handle"):
        robot.move("gripper to the right of the handle")
    if check("the robot's gripper is near the handle and the robot's gripper is not aligned with the handle"):
        robot.put("gripper around handle")
    if check("the robot's gripper is around the handle"):
        robot.pull("handle up")