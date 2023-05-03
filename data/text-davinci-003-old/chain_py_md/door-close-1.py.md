

Steps:
  1. Put gripper above door handle
  2. Drop gripper around door handle
  3. Push door closed

If the gripper is not vertically aligned with the door handle, move the gripper above it.

if check("the robot's gripper is not vertically aligned with door handle"):
    robot.put("gripper above door handle")

If the gripper is almost vertically aligned with the door handle, move it around the handle so it will close it.

if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is not around door handle"):
    robot.drop("gripper around door handle")

Once the gripper is around the door handle, push the door closed.

if check("the robot's gripper is around door handle"):
    robot.push("door closed")