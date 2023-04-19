# Steps:
    #  1. Put gripper above mug handle
    #  2. Drop gripper around mug handle
    #  3. Grab the mug handle
    #  4. Move the mug towards the target location
    if check("the robot's gripper is not above the mug handle"):
        robot.place("gripper above mug handle")
    if check("the robot's gripper is not around mug handle and the robot's gripper is open"):
        robot.drop("gripper around mug handle")
    if check("the robot's gripper is near mug handle and the robot's gripper is open"):
        robot.close("gripper around mug handle")
    if check("the robot's gripper is above mug handle and the robot's gripper is closed"):
        robot.pull("mug to target location")