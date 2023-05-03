

Steps:
1. Put gripper above the cube
2. Drop gripper around the cube
3. Close gripper around the cube
4. Sweep the cube sideways to the target location

First, put the gripper roughly above the cube, so that we don't bump it while
trying to grab it.
if check("the robot's gripper is not above the cube"): 
    robot.move_gripper ("above the cube")

If the gripper isn't around the cube, put it around the cube.
if check("the robot's gripper is not around cube and the robot's gripper is open"):
    robot.move_gripper ("near the cube", close_gripper=True)

If the gripper is near the cube and open, maybe we can grab it by closing the
gripper.
if check("the robot's gripper is above cube and the robot's gripper is closed"):
    robot.move_gripper ("to the left of the cube")

Now that the cube is grasped,we can sweep it sideways to the target location.
if check("the robot's gripper is to the left of the cube"):
    robot.move_gripper ("near the target location")