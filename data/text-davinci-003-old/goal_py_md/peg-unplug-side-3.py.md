

Steps:
  1. Put gripper above the peg
  2. Grab the peg with the gripper 
  3. Line the peg up with the hole
  4. Pull the peg sideways out of the hole

If the robot's gripper is not vertically aligned with the peg, we should move the gripper above the peg.

if check("the robot's gripper is not vertically aligned with the peg"):
    robot.move_gripper("vertically aligned with the peg", close_gripper=True)

Once the gripper is lined up above the peg, we should be able to grab the peg by moving the gripper down around it.

if check("the robot's gripper is vertically aligned with peg and the robot's gripper is not around peg"):
    robot.move_gripper("around the peg")

Once the gripper is around the peg, we need to line it up with the hole.

if check("the peg is not horizontally aligned with hole and the robot's gripper is around peg"):
    robot.move_gripper("horizontally aligned with hole")

Finally, once the peg is lined up with the hole, we can just pull the peg out by i.e. moving the gripper away from the hole.

if check("the robot's gripper is around peg and the peg is horizontally aligned with hole"):
    robot.move_gripper("away from the hole")