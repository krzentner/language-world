The task `handle-press` requires the robot to push down the handle. To do this reliably, the robot should perform the following steps:

Steps: 1. Put gripper above the handle 2. Drop gripper around the handle 3. Push down on the handle

First, position the gripper above the handle.
 - When the robot's gripper is not vertically aligned with the handle, move the robot's gripper until the robot's gripper is vertically aligned with the handle.

Once the gripper is above the handle, move it down around the handle to grab it.
 - When the robot's gripper is above the handle and the gripper is not around the handle, move the robot's gripper until the robot's gripper is around the handle.

Once the handle is grasped, push down on it to execute the task.
 - When the robot's gripper is around the handle, move the robot's gripper until the robot's gripper is pushing down on the handle.