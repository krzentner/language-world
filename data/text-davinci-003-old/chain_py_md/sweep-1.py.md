

Steps:
  1. Put the gripper to the left of the cube
  2. Grab the cube
  3. Align the cube with the target location
  4. Slide the cube to the target location

if check("the robot's gripper is not to the left of the cube"):
    robot.move("gripper to left of cube")
if check("the robot's gripper is to the left of the cube and the robot's gripper is open"):
    robot.grab("cube")
if check("the cube is not aligned with the target location"):
    robot.align("cube to target")
if check("the cube is aligned with the target location"):
    robot.slide("the cube to the target location")