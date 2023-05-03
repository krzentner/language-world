# lever-pull: rotate the lever up
# def lever_pull(robot):
    if check("the robot's gripper is not near the lever handle and the robot's gripper is not vertically aligned with it"):
        robot.put("gripper above lever handle")
    if check("the robot's gripper is vertically aligned with the lever handle and the robot's gripper is not around the handle"):
        robot.drop("gripper around handle")
    if check("the robot's gripper is around the handle and the lever is not rotated"):
        robot.rotate("lever up")