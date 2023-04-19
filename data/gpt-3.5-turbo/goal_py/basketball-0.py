# Steps:
#   1. Put the gripper above the ball
#   2. Grab the ball with the gripper
#   3. Move the gripper towards the hoop
#   4. Release the ball at the right angle to go through the hoop
# First, the gripper should be above the ball to grab it.
if check("the robot's gripper is not vertically aligned with the ball"):
    robot.move_gripper("vertically aligned with the ball")
# Once the gripper is above the ball, close the gripper to grab it.
if check("the robot's gripper is vertically aligned with the ball and the robot's gripper is open"):
    robot.move_gripper("around the ball")
# Move the gripper towards the hoop. We can assume that the hoop is directly
# ahead so there's no need to move the gripper left or right.
if check("the robot's gripper is around the ball and the robot's gripper is not near the hoop"):
    robot.move_gripper("above the hoop")
# Finally, release the ball with the right angle to go through the hoop.
if check("the robot's gripper is near the hoop and the robot's gripper is around the ball"):
    robot.move_gripper("above the ball", open_gripper=True)