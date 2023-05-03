if check("the robot's gripper is not above the mug"):
    robot.move("gripper above mug")
if check("the robot's gripper is open and not around the mug"):
    robot.close("gripper around mug")
if check("the robot's gripper is around the mug and the mug is not near the target location"):
    robot.move("mug to target location")
if check("the mug is near the target location"):
    robot.release("mug at target location")