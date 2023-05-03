# lever-pull: rotate the lever up
def lever_pull(robot):
    if check("the robot's gripper is not near the lever"):
        robot.move("gripper to the left of the lever")
    if check("the robot's gripper is left of the lever"):
        robot.grab("lever")
    if check("the robot's gripper is around the lever"):
        robot.rotate("lever up")