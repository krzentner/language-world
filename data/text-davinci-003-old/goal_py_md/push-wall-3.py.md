

The robot needs to push the puck around a small wall to get to the target location.

Steps:

1. Put gripper in front of puck, keeping the small wall in between
2. Put the gripper around the wall, resting on the wall
3. Push the wall forward and move the puck to the target location 

if check("the robot's gripper is not in front of the puck, with the wall in between"):
    robot.move_gripper("in front of the puck, with the wall in between")
if check("the robot's gripper is not around the wall, resting on it"):
    robot.move_gripper("around the wall, resting on it")
if check("the wall is not in between the puck and the target location"):
    robot.move_gripper("in between the puck and the target location")