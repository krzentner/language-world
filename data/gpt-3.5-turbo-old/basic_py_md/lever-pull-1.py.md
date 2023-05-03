# lever-pull: rotate the lever up
# def lever_pull(robot):
    if check("the robot's gripper is not almost vertically aligned with the lever"):
        robot.put("gripper above lever")
    if check("the robot's gripper is almost vertically aligned with the lever and the robot's gripper is open"):
        robot.put("gripper around lever")
    if check("the robot's gripper is around lever"):
        robot.rotate("lever up")