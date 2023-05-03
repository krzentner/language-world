

We'll need to push the puck onto a small wall, so the robot will need to be careful of its strength when pushing, or the puck might fly off. Let's start by moving the gripper into position.

```
# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
	# Steps:
	#  1. Put gripper above puck
	#  2. Push gripper into top of puck
	#  3. Move the bot to the side of the wall
	#  4. Slide puck to goal
	# Start by putting the gripper above the puck to make sure the puck doesn't fly off.	
	if check("the robot's gripper is not above puck"):
		robot.put("gripper above puck")
	# If the gripper is above the puck, it should be safe to move the robot to 
	# the side of the wall.
	if check("the robot's gripper is above puck"):
		robot.move("bot to side of wall")
	# Now that the robot is ready, slide the puck to the goal.
	if check("the robot's gripper is near the wall and the robot's gripper is above the puck"):
		robot.push("puck against the wall")
		robot.slide("puck to goal")
```

There you have it! The robot will now be able to push a puck to the target location with a small wall in the way.