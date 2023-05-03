

Steps:
  1. Put gripper above lever
  2. Drop gripper around lever
  3. Rotate lever up

If the robot's gripper is not horizontally aligned with the lever, move the gripper near the lever.

if check("the robot's gripper is not horizontally aligned with lever"):
    robot.move_gripper("horizontally aligned with the lever", close_gripper=True)

Once the gripper is in place, rotate the lever up.

if check("the robot's gripper is horizontally aligned with the lever"):
    robot.move_gripper("above the lever")