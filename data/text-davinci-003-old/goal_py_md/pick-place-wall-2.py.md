

Steps:
1. Put gripper above puck
2. Drop gripper around puck
3. Close gripper around puck
4. Move puck to target location

If the robot's gripper is not above the puck, move it above the puck while avoiding the wall in the way.

if check("the robot's gripper is not above the puck"):
    robot.move_gripper("above the puck", avoid="wall")
    
If the robot's gripper is above the puck but not around it, move the gripper around the puck while avoiding the wall.

if check("the robot's gripper is not around the puck and the robot's gripper is open"):
    robot.move_gripper("around the puck", close_gripper=True, avoid="wall")

If the robot's gripper is around the puck but not near the target location, move it near the target location while avoiding the wall. 

if check("the robot's gripper is around the puck and the robot's gripper is not near the target location"):
    robot.move_gripper("near the target location", close_gripper=True, avoid="wall")