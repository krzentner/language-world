
    if check("the robot's gripper is not above mug and the robot's gripper is not vertically aligned with mug"):
        robot.put("gripper above mug")
    if check("the robot's gripper is vertically aligned with mug and the robot's gripper is not around mug"):
        robot.put("gripper around mug")
    if check("the robot's gripper is around mug"):
        robot.push("mug to goal")