 

if check("the robot's gripper is not below the lock dial"):
    robot.move("gripper below lock dial")
if check("the robot's gripper is near the lock dial and the robot's gripper is open"):
    robot.close("gripper around lock dial")
if check("the robot's gripper is below the lock dial and the robot's gripper is closed"):
    robot.turn("clockwise to lock door")