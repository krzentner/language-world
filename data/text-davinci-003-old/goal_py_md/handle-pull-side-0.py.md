

Steps:
 1. Put gripper above the handle
 2. Drop gripper around handle
 3. Pull the handle up

If the robot's gripper is not vertically aligned with the handle, we should move the gripper near the handle to start pulling.

if check("the robot's gripper is not vertically aligned with the handle"):
    robot.move_gripper("vertically aligned with the handle", close_gripper=True)

If the gripper is vertically aligned with the handle but not near it, move the gripper down to the handle to grab it.

if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not near handle"):
    robot.move_gripper("above the handle", close_gripper=True)

Once the gripper is around the handle, we can just pull the handle up.

if check("the robot's gripper is around handle"):
    robot.move_gripper("above the handle")