
    if check("the robot's gripper is not above mug"):
        robot.put("gripper above mug")
    if check("the robot's gripper is not around mug"):
        robot.grab("mug")
    if check("the robot's gripper is around mug"):
        robot.pull("mug to goal")