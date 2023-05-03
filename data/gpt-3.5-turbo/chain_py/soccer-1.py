# Steps:
#  1. Put gripper above ball
#  2. Push gripper into top of ball
#  3. Slide ball to goal
# The robot can push the soccer ball by trapping it by pushing down on it from
# above and moving the gripper.
# If the ball isn't below the gripper as viewed from above, move the gripper
# above the ball.
if check("the robot's gripper is not above the ball and the ball is not in front of the robot's gripper"):
    robot.put("gripper above ball")
# If the gripper is aligned with the ball but not near it, move the gripper
# down to the ball to slide it.
if check("the robot's gripper is above the ball and the ball is not between the gripper's prongs"):
    robot.push("gripper into the ball")
# If the gripper is near the ball, we've probably trapped the ball and can
# slide it to the goal.
# Close the gripper to make sure we keep control of the ball.
if check("the robot's gripper is near the ball and the ball is between the gripper's prongs"):
    robot.slide("the ball to the goal")