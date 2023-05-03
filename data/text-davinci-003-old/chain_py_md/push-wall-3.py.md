

Steps:
1. Put gripper near or above the puck
2. Push gripper into the puck while avoiding the wall
3. Push puck to the goal

If the robot's gripper is not near or above the puck, move the gripper to the puck.
if check("the robot's gripper is not near or above puck"):
    robot.put("gripper near or above puck")

If the robot's gripper is near the puck, move the gripper so it is pushing the puck away from the wall.
if check("the robot's gripper is near puck"):
    robot.push("the gripper into the puck while avoiding the wall")

Once the puck is pushed away from the wall, move it to the goal.
if check("the puck is pushed away from the wall"):
    robot.move("the puck to the goal")