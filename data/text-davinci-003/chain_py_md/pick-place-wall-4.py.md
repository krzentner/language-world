

The steps for this task would be similar to those for `pick-place`:

# Steps:
#  1. Put gripper above puck
#  2. Drop gripper around puck
#  3. Close gripper around puck
#  4. Move puck to goal, facing the wall
#  5. Move gripper to front of puck
#  6. Push the puck sideways against the wall
#  7. Pull the puck back from the wall
#  8. Move the puck to the goal

First, put the gripper roughly above puck, so that we don't bump it while
trying to grab it.

if check("the robot's gripper is not above the puck"):
    robot.place("gripper above puck")

If the gripper isn't around the puck, put it around the puck

if check("the robot's gripper is not around puck and the robot's gripper is open"):
    robot.drop("gripper around puck")

If the gripper is near the puck and open, maybe we can grab it by closing
the gripper

if check("the robot's gripper is near puck and the robot's gripper is open"):
    robot.close("gripper around puck")

We closed the gripper, and the puck is still near the gripper, so maybe we
grabbed it. Try to move the puck to the goal

if check("the robot's gripper is above puck and the robot's gripper is closed"):
    robot.move("puck to goal, facing wall")

To get the puck around the wall, we'll need the gripper to be in front of the 
puck. Move the gripper in front of the puck

if check("the robot's gripper is not in front of puck"):
    robot.move("gripper to front of puck")

Once the gripper is in front, start pushing the puck against the wall to get it
around the corner

if check("the robot's gripper is in front of puck"):
    robot.push("puck sideways against wall")

Once the puck is pushed against the wall, pull back from the wall so it can get 
around the corner

if check("the puck is against wall"):
    robot.pull("puck back from wall")

Finally, move the puck to the goal

if check("the puck isn't against wall"):
    robot.move("puck to goal")