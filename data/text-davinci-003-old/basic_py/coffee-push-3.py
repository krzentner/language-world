
    if check("the robot's gripper is not above mug"):
        robot.put("gripper above mug")
    if check("the robot's gripper is above mug and the robot's gripper is open"):
        robot.grab("mug")
    if check("the robot's gripper is around mug and the mug is not at goal"):
        robot.slide("mug to goal")