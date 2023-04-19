

Steps:
1. Put gripper above the puck
2. Push gently against the wall, so that the puck can move
3. Push the puck to the goal

First, put the gripper roughly above the puck, so that we don't bump it while trying to grab it.
if check("the robot's gripper is not above the puck"):
    robot.place("gripper above puck")

Next, we'll gently push against the wall so the puck can slide to the goal.
if check("the robot's gripper is not gently pushing against wall"):
    robot.push("gently against wall")

Finally, push the puck to the goal. This should be easy since we already moved the wall out of the way.
if check("puck is not near goal"):
    robot.slide("puck to goal")