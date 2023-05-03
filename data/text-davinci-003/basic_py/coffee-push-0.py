
    if check("the robot's gripper is not above mug and the robot's gripper is not near mug"):
        robot.put("gripper above mug")
    if check("the robot's gripper is above the mug and the robot's gripper is not around mug"):
        robot.grab("mug")
    if check("the robot's gripper is around mug"):
        robot.push("mug to target")
    if check("the robot's gripper is not forward aligned with mug"):
        robot.place("mug at target")