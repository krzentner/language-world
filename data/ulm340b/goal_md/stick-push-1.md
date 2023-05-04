


Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.


The task `button-press-side` requires the robot to press the button from the side.
To press the button from the side reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above button  2. Drop gripper around button  3. Press button by closing gripper
    We need to put the gripper above the button before we can grab it, because of the angle of the robot's gripper.
    - When the robot's gripper is not above button, move the robot's gripper until the robot's gripper is above button
    Once the gripper is lined up above the button, we should be able to grab the button by moving the gripper down around it.
    - When the robot's gripper is above button and the robot's gripper is not around button, move the robot's gripper until the robot's gripper is around button and the robot's gripper is closed
    Once the gripper is around the button, we can just press the button by closing the gripper more.
    - When the robot's gripper is around button, move the robot's gripper until the robot's gripper is closed

The task `drawer-open` requires the robot to pull the drawer open.
To pull the drawer open reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above drawer handle  2. Drop gripper around drawer handle  3. Pull open the drawer
    We need to put the gripper above the drawer handle before we can grab it, because of the angle of the robot's gripper.
    - When the robot's gripper is not above drawer handle, move the robot's gripper until the robot's gripper is above drawer handle
    Once the gripper is lined up above the drawer handle, we should be able to grab the drawer handle by moving the gripper down around it.
    - When the robot's gripper is above drawer handle and the robot's gripper is not around drawer handle, move the robot's gripper until the robot's gripper is around drawer handle
    Once the gripper is around the drawer handle, we can just pull the drawer open.
    - When the robot's gripper is around drawer handle, move the robot's gripper until the robot's gripper is left of the drawer handle

The task `door-open` requires the robot to pull the door open.
To pull the