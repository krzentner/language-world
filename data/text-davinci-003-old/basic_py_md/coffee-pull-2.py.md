

if check("the robot's gripper is not near the mug"):
    robot.reach("until the mug is in grip")
if check("the robot's gripper is around mug"):
    robot.pull("the mug to target location")