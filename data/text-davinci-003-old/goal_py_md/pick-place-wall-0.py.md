

Steps:
1. Put gripper above puck, but far enough away from the wall so it can fit between the wall and the puck
2. Drop gripper around puck
3. Close gripper around puck
4. Move puck to goal

First, we need to put the gripper above the puck, but far enough away from the wall that it can fit between the wall and the puck.
if check("the robot's gripper is not above the puck and the robot's gripper is not far enough away from wall"):
    robot.move_gripper("above the puck", far_from_wall=True)

Once the gripper is far enough away from the wall, if it isn't around the puck, put it around the puck.
if check("the robot's gripper is not around puck and the robot's gripper is open"):
    robot.move_gripper("near the puck", close_gripper=True)

If the gripper is near the puck and open, maybe we can grab it by closing the gripper.
if check("the robot's gripper is above puck and the robot's gripper is closed"):
    robot.move_gripper("above the target location")