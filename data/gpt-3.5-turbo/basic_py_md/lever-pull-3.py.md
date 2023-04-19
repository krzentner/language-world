# lever-pull: rotate the lever up
# def lever_pull(robot):
    if check("the robot's gripper is not near the lever and the robot's gripper is not horizontally aligned with the lever"):
        robot.move("gripper to the left of the lever")
    if check("the robot's gripper is horizontally aligned with the lever and the robot's gripper is not around the lever"):
        robot.put("gripper around the lever")
    if check("the robot's gripper is around the lever and the robot's gripper is not vertically aligned with the lever"):
        robot.move("gripper slightly above lever")
    if check("the robot's gripper is slightly above the lever and the robot's gripper is not forward aligned with the lever"):
        robot.move("gripper forward")
    if check("the robot's gripper is forward aligned with the lever"):
        robot.pull("lever up")