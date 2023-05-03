# Steps:
#  1. Put gripper above ball
#  2. Drop gripper around ball
#  3. Close gripper around ball
#  4. Push ball to goal
# First, put the gripper roughly above the soccer ball.
if check("the robot's gripper is not above the soccer ball"):
    robot.put("gripper above soccer ball")
# If the gripper isn't around the soccer ball, put it around the soccer ball.
if check("the robot's gripper is not around soccer ball and the robot's gripper is open"):
    robot.drop("gripper around soccer ball")
# If the gripper is near the soccer ball and open, maybe we can grab it by closing
# the gripper.
if check("the robot's gripper is near soccer ball and the robot's gripper is open"):
    robot.close("gripper around soccer ball")
# We closed the gripper, and the soccer ball is still near the gripper, so maybe we
# grabbed it.
# Try to push the soccer ball to the goal.
# If we didn't grab it, we'll just go back to an earlier step.
if check("the robot's gripper is above soccer ball and the robot's gripper is closed"):
    robot.push("soccer ball to the goal")