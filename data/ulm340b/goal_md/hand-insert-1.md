
''',
'test2-goal-desc': '''
You will now be given a sequence of tasks and be asked to provide plans for the robot to complete these tasks.
The task `button-press-front` requires the robot to push the button from the front.
To push the button from the front reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from the front  2. Push down on the button from the front
    - When the robot's gripper is not horizontally aligned with button, move the robot's gripper until the robot's gripper is horizontally aligned with the button and the robot's gripper is open
    - When the robot's gripper is horizontally aligned with button, move the robot's gripper until the robot's gripper is above the button

The task `drawer-open` requires the robot to pull the drawer open.
To pull the drawer open reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above drawer handle  2. Drop gripper around drawer handle  3. Pull open the drawer
    - When the robot's gripper is not vertically aligned with drawer handle, move the robot's gripper until the robot's gripper is vertically aligned with the drawer handle
    - When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, move the robot's gripper until the robot's gripper is around the drawer handle
    - When the robot's gripper is around drawer handle, move the robot's gripper until the robot's gripper is horizontally aligned with the drawer handle

The task `drawer-close` requires the robot to push the drawer close.
To push the drawer close reliably, the robot should perform the following steps:
    Steps:  1. Put gripper roughly around the drawer handle  2. Push the drawer closed
    - When the robot's gripper is not near the drawer handle, move the robot's gripper until the robot's gripper is near the drawer handle
    - When the robot's gripper is forward aligned with drawer handle, move the robot's gripper until the robot's gripper is around the drawer handle

The task `door-open` requires the robot to pull the door open.
To pull the door open reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above door handle  2. Drop gripper around door handle  3. Pull open the door
    - When the robot's gripper is not almost vertically aligned with door handle, move the robot's gripper until the