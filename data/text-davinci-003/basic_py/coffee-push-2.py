
    if check("the robot's gripper is not vertically aligned with mug"):
        robot.put("gripper above mug")
    if check("the robot's gripper is vertically aligned with mug and the robot's gripper is not around mug"):
        robot.put("gripper around mug")
    if check("the robot's gripper is around mug and mug is not left of robot's gripper"):
        robot.grab("mug")
    if check("mug is left of robot's gripper"):
        robot.push("mug to goal")