
    Steps:  1. Put gripper above drawer handle  2. Drop gripper around drawer handle  3. Push open the drawer
    We need to put the gripper above the drawer handle before we can grab it, because of the angle of the robot's gripper.
    - When the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer handle.
    Once the gripper is lined up above the drawer handle, we should be able to grab the drawer handle by moving the gripper down around it.
    - When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, the robot should put gripper around drawer handle.
    Once the gripper is around the drawer handle, we can just push the drawer open.
    - When the robot's gripper is around drawer handle, the robot should push into drawer.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above door handle  2. Drop gripper around door handle  3. Push closed the door
    First, put the gripper mostly above the door handle.
    - When the robot's gripper is not almost vertically aligned with door handle, the robot should put gripper above door handle.
    As long as the gripper is almost lined up, closing it should line it up all the way.
    - When the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open, the robot should put gripper around door handle.
    As long as the gripper is still vertically aligned with the door handle, it's being closed, so keep pushing.
    - When the robot's gripper is vertically aligned with the door handle, the robot should push door closed.

The task `drawer-open-side` requires the robot to grab the drawer handle and open it.
To grab the drawer handle and open it reliably, the robot should perform the following steps:
    Steps:  1. Put gripper left of drawer handle  2. Drop gripper around drawer handle  3. Pull open the drawer
    Because this is `open-side`, the drawer handle is long, so just check if the gripper is aligned in front of it.
    If the gripper is not aligned in front of the drawer handle, line up the gripper in front of the drawer handle.
    - When the robot's gripper is not horizontally aligned with drawer handle and the robot's gripper is