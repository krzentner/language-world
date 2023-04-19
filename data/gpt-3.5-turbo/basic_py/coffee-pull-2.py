if check("mug is not within the robot's reach"):
        robot.move("to the location of the mug")
    if check("the robot's gripper is not above the handle of the mug and the robot's gripper is not vertically aligned with the mug"):
        robot.put("gripper above the mug's handle")
    if check("the robot's gripper is vertically aligned with the mug's handle and the robot's gripper is not around the handle"):
        robot.grab("the handle of the mug")
    if check("the robot's gripper is around the handle and the mug is not at the target location"):
        robot.pull("the mug to the target location")