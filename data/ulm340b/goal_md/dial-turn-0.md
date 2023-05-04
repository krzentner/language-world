


When the robot's gripper is not above the dial, move the robot's gripper until the robot's gripper is above the dial
When the robot's gripper is above the dial, move the robot's gripper until the robot's gripper is above the dial and the robot's gripper is closed
When the robot's gripper is above the dial, move the robot's gripper until the robot's gripper is above the dial
When the robot's gripper is above the dial, move the robot's gripper until the robot's gripper is above the dial
When the robot's gripper is above the dial, move the robot's gripper until the robot's gripper is above the dial

Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.


The task `door-open` requires the robot to pull the door open.
To pull the door open reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above door handle  2. Drop gripper around door handle  3. Pull open the door
    First, put the gripper mostly above the door handle.
    - When the robot's gripper is not almost vertically aligned with door handle, move the robot's gripper until the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is closed
    As long as the gripper is almost lined up, closing it should line it up all the way.
    - When the robot's gripper is vertically aligned with the door handle, move the robot's gripper until the robot's gripper is left of the door handle

The task `reach` requires the robot to reach to the target location.
To reach to the target location reliably, the robot should perform the following steps:
    Steps:  1. Reach towards the target
    We don't have any objects to manipulate, so we can just move the robot's gripper directly to the target location
    - When the robot's gripper is not near reach target, move the robot's gripper until the robot's gripper is near the reach target

The task `drawer-close` requires the robot to push the drawer close.
To push the drawer close reliably, the robot should perform the following steps:
    Steps:  1. Put gripper roughly around the drawer handle  2. Push the drawer closed
    If the gripper is not near the drawer handle, move it to the drawer handle. We don't need to be careful about the direction, since the