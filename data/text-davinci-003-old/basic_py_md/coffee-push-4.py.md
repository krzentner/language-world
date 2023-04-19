

if check("the robot's gripper is not above the mug"):
    robot.place("gripper above mug")
if check("the robot's gripper is not around mug and the robot's gripper is open"):
    robot.drop("gripper around mug")
if check("the robot's gripper is around mug and the robot's gripper is open"):
    robot.close("gripper around mug")
if check("the robot's gripper is near the mug and the mug is below the robot's gripper"):
    robot.slide("mug to the goal")