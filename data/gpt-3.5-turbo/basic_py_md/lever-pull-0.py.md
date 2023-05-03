# lever-pull: rotate the lever up
def lever_pull(robot):
    if check("the robot's gripper is not near the lever handle"):
        robot.move("gripper to left of lever handle")
    if check("the robot's gripper is in front of the lever handle"):
        robot.grab("lever handle")
    if check("the robot's gripper is around lever handle"):
        robot.twist("lever up")