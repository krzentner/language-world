if check("the robot's gripper is not above the mug"):
        robot.place("gripper above mug")
    if check("the robot's gripper is not around the mug and the robot's gripper is open"):
        robot.drop("gripper around mug")
    if check("the robot's gripper is near mug and the robot's gripper is open"):
        robot.close("gripper around mug")
    if check("the robot's gripper is above mug and the robot's gripper is closed"):
        robot.lift("the mug")
    if check("the robot's gripper is not above the target location"):
        robot.move("gripper to the target location")
    if check("the mug is not at the target location"):
        robot.put("the mug at the target location")