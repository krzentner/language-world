# Steps:
#  1. Put the gripper above the soccer ball
#  2. Drop gripper around soccer ball
#  3. Push soccer ball into target location
# First, put the gripper roughly above the soccer ball so we don't hit it
# accidentally while grabbing it.
if check("the robot's gripper is not above the soccer ball"):
    robot.move_gripper("above the soccer ball")
# If the gripper is above the soccer ball, grab the ball if the gripper is open
# and move it towards the target location.
if check("the robot's gripper is above the soccer ball and the gripper is open"):
    robot.move_gripper("near the target location")