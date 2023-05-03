# lever-pull: rotate the lever up
# def lever_pull(robot):
if check("the robot's gripper is not near the lever handle"):
    robot.reach("lever handle")
if check("the robot's gripper is near the lever handle"):
    robot.grab("lever handle")
if check("the robot's gripper is holding the lever handle and the lever is not fully rotated"):
    robot.rotate("lever up")