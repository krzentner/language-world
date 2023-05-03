

Steps:
1. Place the gripper in front of the ball
2. Grab the ball with the gripper
3. Move the ball to the hoop
4. Lift up the ball and move it above the hoop
5. Drop the ball into the hoop

if check("the robot's gripper is not in front of the ball"):
    robot.move_gripper("in front of the ball", close_gripper=True)

if check("the robot's gripper is in front of the ball and the ball is not in the gripper"):
    robot.move_gripper("around the ball")

if check("the robot's gripper is around the ball"):
    robot.move_gripper("near the hoop")

if check("the robot's gripper is near the hoop and the ball is not above the hoop"):
    robot.move_gripper("above the hoop")

if check("the robot's gripper is above the hoop"):
    robot.move_gripper("near the hoop", close_gripper= False)