# lever-pull: rotate the lever up
def lever_pull(robot):
    if check("the robot's gripper is not near the lever and the lever is not in the up position"):
        robot.reach("to lever")
    if check("the robot's gripper is near the lever and the lever is not in the up position"):
        robot.push("the gripper into lever")
    if check("the robot's gripper is in the lever and the lever is not in the up position"):
        robot.rotate("the gripper up and back")