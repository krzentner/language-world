:
    Steps:  1. Put gripper above handle  2. Drop gripper around handle  3. Pull handle up
    First, put the gripper above the handle.
    - When the robot's gripper is not vertically aligned with handle, the robot should put gripper above handle.
    Once the gripper is lined up above the handle, we should be able to grab the handle by moving the gripper down around it.
    - When the robot's gripper is vertically aligned with handle and the robot's gripper is not around handle, the robot should put gripper around handle.
    Once the gripper is around the handle, we can just pull the handle up.
    - When the robot's gripper is around handle, the robot should lift handle.

The task `pick-out-of-hole` requires the robot to pick the puck up out of the hole.
To pick the puck up out of the hole reliably, what steps the robot should perform?:
    Steps:  1. Put gripper above puck  2. Drop gripper around puck  3. Close gripper around puck  4. Slide the puck out of the hole
    The puck is in a small hole so we'll have to put the gripper above the puck.
    - When the robot's gripper is not above puck, the robot should put gripper above puck.
    Once the gripper is above the puck, put the gripper around the puck.
    - When the robot's gripper is above puck and the robot's gripper is not around puck, the robot should drop gripper around puck.
    Once the gripper is near the puck, close it.
    - When the robot's gripper is near puck and the robot's gripper is open, the robot should close gripper around puck.
    If the puck is still near the robot's gripper, it should be in the gripper. Slide the puck out of the hole.
    - When the robot's gripper is above puck and the robot's gripper is closed, the robot should slide puck out of hole.

The task `handle-pull-front` requires the robot to pull up the handle from the front.
To pull up the handle from the front reliably, what steps the robot should perform?:
    Steps:  1. Put gripper above handle  2. Grab handle with gripper  3. Pull the handle up
    First, put the gripper above the handle.
    - When the robot's gripper is not vertically aligned with handle, the robot should put gripper above handle.
   