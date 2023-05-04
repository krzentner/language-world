
    Steps:  1. Move gripper around the handle  2. Push down on the handle
    First, put the gripper around the handle.
    - When the robot's gripper is above the handle, move the robot's gripper until the robot's gripper is around the handle
    If the gripper is already below the handle, push the handle down.
    - When the robot's gripper is around the handle, move the robot's gripper until the robot's gripper is below the handle


The task `drawer-close` requires the robot to push the drawer close.
To push the drawer close reliably, what steps the robot should perform?
    Steps:  1. Put gripper roughly around the drawer handle  2. Push the drawer closed
    If the gripper is not near the drawer handle, move it to the drawer handle. We don't need to be careful about the direction, since the drawer is large and we're just pushing it (unlike when opening the drawer).
    - When the robot's gripper is not near the drawer handle, move the robot's gripper until the robot's gripper is near the drawer handle
    If the drawer is aligned with the gripper as seen from in front, we can push the drawer closed.
    - When the robot's gripper is forward aligned with drawer handle, move the robot's gripper until the robot's gripper is around the drawer handle


The task `drawer-open` requires the robot to pull the drawer open.
To pull the drawer open reliably, what steps the robot should perform?
    Steps:  1. Put gripper above drawer handle  2. Drop gripper around drawer handle  3. Pull open the drawer
    We need to put the gripper above the drawer handle before we can grab it, because of the angle of the robot's gripper.
    - When the robot's gripper is not vertically aligned with drawer handle, move the robot's gripper until the robot's gripper is vertically aligned with the drawer handle
    Once the gripper is lined up above the drawer handle, we should be able to grab the drawer handle by moving the gripper down around it.
    - When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, move the robot's gripper until the robot's gripper is around the drawer handle
    Once the gripper is around the drawer handle, we can just pull the drawer open.
    - When the robot's gripper is around drawer handle, move the robot's gripper until the robot's