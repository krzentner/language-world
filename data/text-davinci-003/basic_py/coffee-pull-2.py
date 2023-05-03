
    if check("the robot's gripper is not above the mug"):
        robot.put("gripper above mug")
    if check("the robot's gripper is above the mug and the robot's gripper is not around mug"):
        robot.put("gripper around mug")
    if check("the robot's gripper is around mug and the mug is not near goal"):
        robot.pull("mug to goal")