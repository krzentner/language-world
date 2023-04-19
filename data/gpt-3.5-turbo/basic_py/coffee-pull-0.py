if check("the robot's gripper is not above the handle of the mug"):
        robot.place("gripper above mug handle")
    if check("the robot's gripper is not around the handle of the mug and the robot's gripper is open"):
        robot.drop("gripper around mug handle")
    if check("the robot's gripper is near the handle of the mug and the robot's gripper is open"):
        robot.close("gripper around mug handle")
    if check("the robot's gripper is above the handle of the mug and the mug is not at the target location"):
        robot.pull("mug towards the target location")
    if check("the mug is at the target location"):
        robot.release("gripper and let go of mug")