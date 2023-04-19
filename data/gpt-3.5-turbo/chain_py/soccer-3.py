# Steps:
#   1. Put the gripper above soccer ball
#   2. Grab the soccer ball
#   3. Move the soccer ball towards the goal
# We need to put the gripper above the soccer ball to grab it.
if check("the robot's gripper is not above the soccer ball"):
    robot.place("gripper above soccer ball")
# Once the gripper is above the soccer ball, we can try to grab the soccer ball.
if check("the robot's gripper is above the soccer ball" and "the robot's gripper is open"):
    robot.pick_up("soccer ball")
# If the soccer ball is in the gripper, we can try to move it towards the goal.
if check("the soccer ball is in the gripper"):
    robot.move("soccer ball towards goal")