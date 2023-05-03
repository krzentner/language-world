The steps the robot should perform for the task `handle-pull` to reliably pull up the handle are:

    Steps:  1. Put gripper above the handle  2. Drop gripper around the handle  3. Pull up the handle
    First, put the gripper above the handle.
    - When the robot's gripper is not vertically aligned with the handle, move the robot's gripper until the robot's gripper is vertically aligned with the handle and the robot's gripper is closed
    Once the gripper is lined up above the handle, we should be able to grab the handle by moving the gripper down around it.
    - When the robot's gripper is vertically aligned with the handle and the robot's gripper is not around the handle, move the robot's gripper until the robot's gripper is around the handle
    Once the gripper is around the handle, we can simply pull up the handle.
    - When the robot's gripper is around the handle, move the robot's gripper until the handle is pulled up completely.