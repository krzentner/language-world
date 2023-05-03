# lever-pull: rotate the lever up
def lever_pull(robot):
    if check("the robot's gripper is not vertically aligned with the lever and the robot's gripper is below the lever"):
        robot.move("gripper to right of lever")
        robot.put("gripper above lever")
    if check("the robot's gripper is almost vertically aligned with the lever and the robot's gripper is open"):
        robot.put("gripper around lever")
    if check("the robot's gripper is vertically aligned with the lever and the robot's gripper is closed"):
        robot.rotate("lever up")