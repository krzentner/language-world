
    - When the robot's gripper is not vertically aligned with the puck, move the robot's gripper until the robot's gripper is vertically aligned with the puck
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, move the robot's gripper until the robot's gripper is above the puck and the robot's gripper is closed
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, move the robot's gripper until the robot's gripper is above the target location

The task `drawer-open-topdown` requires the robot to pull the drawer open.
To pull the drawer open reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from above  2. Drop gripper around drawer handle  3. Pull open the drawer
    Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
    - When the robot's gripper is not vertically aligned with drawer handle, move the robot's gripper until the robot's gripper is vertically aligned with the drawer handle
    Now that the gripper is lined up, just put it around the drawer handle to grab it.
    - When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, move the robot's gripper until the robot's gripper is around the drawer handle
    Once the gripper is around the drawer handle, we can just pull the drawer open.
    - When the robot's gripper is around drawer handle, move the robot's gripper until the robot's gripper is horizontally aligned with the drawer handle

The task `door-open-topdown` requires the robot to pull the door open.
To pull the door open reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from above  2. Drop gripper around door handle  3. Pull open the door
    Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
    - When the robot's gripper is not vertically aligned with door handle, move the robot's gripper until the robot's gripper is vertically aligned with the door handle
    Now that the gripper is lined up, just put it around the door handle to grab it.
    - When the robot's gripper is vertically aligned with door handle and the