

If check("the robot's gripper is not near the mug"):
    robot.reach("to mug")

If check("the robot's gripper is not around mug"):
    robot.place("gripper around mug")

If check ("the robot's gripper is around mug"):
    robot.push("mug to target")