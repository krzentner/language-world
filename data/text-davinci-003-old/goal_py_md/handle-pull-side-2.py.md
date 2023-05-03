

Steps:
1. Put gripper left of the handle
2. Drop gripper around the handle
3. Pull up the handle

If the robot's gripper is not near the handle, we need to put the robot's gripper near it to be able to grab the handle.

if check("the robot's gripper is not near the handle"):
    robot.move_gripper("left of the handle")

If the gripper is not around the handle, drop the gripper around it.

if check("the robot's gripper is not around the handle and the robot's gripper is open"):
    robot.move_gripper("near the handle", close_gripper=True)

Once the gripper is around the handle, we can just pull up the handle.

if check("the robot's gripper is around the handle"):
    robot.move_gripper("up of the handle")