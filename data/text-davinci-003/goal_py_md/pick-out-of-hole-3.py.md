

Steps:
  1. Put gripper above hole
  2. Drop gripper around peg
  3. Close gripper around peg
  4. Pull peg out of hole
  5. Move peg to goal

First, put the gripper roughly above the hole, so that we don't bump the peg while trying to grab it.
if check("the robot's gripper is not above the hole"):
    robot.move_gripper("above the hole")

If the gripper isn't around the peg, put it around the peg and close the gripper to grab it.
if check("the robot's gripper is not around peg and the robot's gripper is open"):
    robot.move_gripper("near the peg", close_gripper=True)

Because the peg is stuck in the hole, it's important that the gripper is placed on the right side of the peg, so that the gripper can pull the peg out of the hole. 
if check("the robot's gripper is around peg, but not on the right side of the peg"):
    robot.move_gripper("right side of the peg")

Now that the gripper is on the right side of the peg, we can pull the peg out of the hole by moving the gripper slightly up.
if check("the robot's gripper is on the right side of the peg"):
    robot.move_gripper("above the peg")

Finally, we can move the peg to the goal location.
if check("the robot's gripper is above peg"):
    robot.move_gripper("above the target location")