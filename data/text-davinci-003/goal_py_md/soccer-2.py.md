

Steps:
1. Put gripper above soccer ball
2. Drop gripper around soccer ball
3. Push soccer ball to the target location

if check("the robot's gripper is not above the soccer ball"):
    robot.move_gripper("above the soccer ball")

if check("the robot's gripper is not around soccer ball and the robot's gripper is open"):
    robot.move_gripper("near the soccer ball", close_gripper=True)

if check("the robot's gripper is near the soccer ball and the robot's gripper is closed"):
    robot.move_gripper("above the target location")