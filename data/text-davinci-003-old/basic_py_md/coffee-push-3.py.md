

If check("the robot's gripper is not near the mug"):
    robot.move("gripper to the mug")
if check("the robot's gripper is near the mug"):
    robot.grab("mug")
if check("the robot's gripper is holding mug and the mug is not above the goal place"):
    robot.move("mug to the goal")
if check("the robot's gripper is holding mug and the mug is near the goal place"):
    robot.place("mug at the goal")