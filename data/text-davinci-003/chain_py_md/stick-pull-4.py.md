

Steps:
1. Put the gripper between the stick and the thermos.
2. Push the gripper against the stick.
3. Pull the gripper with the stick.
4. Move the stick and thermos to the target location.

if check("the robot's gripper is not between the stick and thermos"):
    robot.put("gripper between stick and thermos") 
if check("the robot's gripper is between the stick and thermos and the robot's gripper is not pushing against the stick"):
    robot.push("gripper against stick")
if check("the robot's gripper is pushing against the stick"):
    robot.pull("gripper with stick")
if check("the gripper is pulling the stick"):
    robot.move("stick and thermos to goal location")