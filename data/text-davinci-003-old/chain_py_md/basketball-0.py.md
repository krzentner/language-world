

Steps:
1. Put the gripper above the ball
2. Drop the gripper around the ball
3. Close the gripper around the ball
4. Line up the ball with the hoop
5. Throw the ball into the hoop

if check("the robot's gripper is not above the ball"):
    robot.put("gripper above ball")
if check("the robot's gripper is not around the ball and the robot's gripper is open"):
    robot.drop("gripper around ball")
if check("the robot's gripper is near the ball and the robot's gripper is open"):
    robot.close("gripper around ball")
if check("the ball is not horizontally aligned with the hoop"):
    robot.align("ball to hoop")
if check("the ball is horizontally aligned with the hoop"):
    robot.throw("ball into hoop")