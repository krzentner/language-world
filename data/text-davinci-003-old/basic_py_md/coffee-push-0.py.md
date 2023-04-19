

if check("the robot's gripper is not near the mug"):
    robot.reach("mug")
if check("the robot's gripper is not around the mug and the robot's gripper is open"):
    robot.drop("gripper around mug")
if check("the robot's gripper is near the mug and the robot's gripper is open"):
    robot.close("gripper around mug")
if check("the robot's gripper is around the mug and the robot's gripper is closed"):
    robot.move("mug to goal")