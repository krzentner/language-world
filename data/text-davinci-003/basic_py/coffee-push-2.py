
    if check("the robot's gripper is not near the mug"):
        robot.reach("to mug")
    if check("the robot's gripper is not around the mug"):
        robot.drop("gripper around mug")
    if check("the robot's gripper is near the mug"):
        robot.push("mug to goal")