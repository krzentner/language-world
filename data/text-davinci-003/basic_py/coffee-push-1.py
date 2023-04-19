
    if check("the robot's gripper is not vertically aligned with the mug handle and the robot's gripper is below the mug handle"):
        robot.put("gripper above mug handle")
    if check("the robot's gripper is vertically aligned with the mug handle and the robot's gripper is not around the mug handle"):
        robot.drop("gripper around mug handle")
    if check("the robot's gripper is near the mug and the mug is below the robot's gripper"):
        robot.slide("mug to the goal")